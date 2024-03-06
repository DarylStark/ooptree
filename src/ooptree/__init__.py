"""OOPTree.

A CLI tool to visualize class hierarchies.
"""

from rich.console import Console

from .class_finder import ClassFinder
from .ooptree import OOPTree
from .ooptree_printer import OOPTreePrinter


def print_tree(
    base_class_name: str | type,
    modules: list[str] | None = None,
) -> None:
    """Print a tree for a specific class."""
    if isinstance(base_class_name, str):
        # Configure the finder
        finder = ClassFinder(base_class_name)
        if modules:
            for module in modules:
                finder.add_module(module)
        # Get the base class
        base_class = finder.get_class()
    elif isinstance(base_class_name, type):
        base_class = base_class_name
    else:
        raise TypeError('Argument "base_class_name" should be a str or a type')

    # Create a Rich Console
    console = Console()

    # Print the OOP Tree
    tree = OOPTree(base_class)
    printer = OOPTreePrinter(tree)
    printer.print_to_console(console)


__version__ = '0.0.0-dev'
