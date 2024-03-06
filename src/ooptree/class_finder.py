"""Module that contains the ClassFinder class."""

import builtins
from abc import ABC, abstractmethod
from importlib import import_module
from typing import Any


class ClassNotFoundError(Exception):
    """Exception when the class wasn't found."""


class Finder(ABC):
    """Interface for finders."""

    def __init__(self) -> None:
        """Set default values."""
        self._next_finder: 'Finder' | None = None

    def set_next(self, next_finder: 'Finder') -> 'Finder':
        """Set the next finder in the chain.

        Args:
            next_finder: the next finder in the chain.

        Returns:
            Itself, so the requests can be chained.
        """
        self._next_finder = next_finder
        return next_finder

    @abstractmethod
    def find(self, class_name: str, class_finder: 'ClassFinder') -> type:
        """Walk through the chain to find the class.

        Args:
            class_name: the class name to search.
            class_finder: the instance of the ClassFinder class.

        Raises:
            ClassNotFoundError: when the class couldn't be found.
        """
        if self._next_finder:
            return self._next_finder.find(class_name, class_finder)
        raise ClassNotFoundError


class DynamicModuleFinder(Finder):
    """Finder to search dynamic module imports."""

    def find(self, class_name: str, class_finder: 'ClassFinder') -> type:
        """Search in dyanmic module imports for the class.

        Args:
            class_name: the class name to search for.
            class_finder: the instance of the ClassFinder class.
        """
        for dynamic_module in class_finder.dynamic_modules:
            class_object = getattr(dynamic_module, class_name, None)
            if class_object:
                return class_object
        return super().find(class_name, class_finder)


class GlobalFinder(Finder):
    """Finder to search the global namespace."""

    def find(self, class_name: str, class_finder: 'ClassFinder') -> type:
        """Search in the global namespace for the class.

        Args:
            class_name: the class name to search for.
            class_finder: the instance of the ClassFinder class.
        """
        class_object = globals().get(class_name, None)
        if class_object:
            return class_object
        return super().find(class_name, class_finder)


class BuiltinFinder(Finder):
    """Finder to search the Builtin namespace."""

    def find(self, class_name: str, class_finder: 'ClassFinder') -> type:
        """Search in the builtins namespace for the class.

        Args:
            class_name: the class name to search for.
            class_finder: the instance of the ClassFinder class.
        """
        class_object = getattr(builtins, class_name, None)
        if class_object:
            return class_object
        return super().find(class_name, class_finder)


class ClassFinder:
    """Finds a class based on the string-representation of the class."""

    def __init__(self, class_name: str) -> None:
        """Set default values.

        Args:
            class_name: the name of the class.
        """
        self.dynamic_modules: list[Any] = []
        self._class_name = class_name

        # Set the chain to find the class
        self._first_finder: Finder = DynamicModuleFinder()
        self._first_finder.set_next(GlobalFinder()).set_next(BuiltinFinder())

    def add_module(self, *modules: str) -> None:
        """Add modules to the dynamic imports."""
        for module in modules:
            self.dynamic_modules.append(import_module(module))

    def get_class(self) -> type:
        """Get the class object.

        Finds the class object for the given classname by searching specific
        sources.

        Returns:
            The class object for the given classname.
        """
        return self._first_finder.find(self._class_name, self)
