"""Module with `OOPTree` class."""


class OOPTree:
    """Class that finds the tree for a parent class."""

    def __init__(self, parent_class: type) -> None:
        """Set default values.

        Args:
            parent_class: the parent class for the tree.
        """
        self.class_name = parent_class.__name__
        self.class_name_parents = [
            base.__name__
            for base in parent_class.__bases__
            if base.__name__ != 'object'
        ]
        self.children: list[OOPTree] = []

        if len(parent_class.__subclasses__()):
            self.children = [
                OOPTree(subclass) for subclass in parent_class.__subclasses__()
            ]

    def is_leaf(self) -> bool:
        """Get if this is a leaf object.

        Check if this Tree is a leaf object. A leaf object doesn't have any
        child classes.

        Returns:
            True if this Tree has no children. Otherwise False.
        """
        return len(self) == 0

    def __len__(self) -> int:
        """Get the number of children in the class."""
        return len(self.children)
