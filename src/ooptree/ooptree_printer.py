"""Module with a Console printer for a OOPTree object."""

from rich.console import Console
from rich.tree import Tree

from ooptree.ooptree import OOPTree


class OOPTreePrinter:
    """Class to print a OOPTree to console."""

    def __init__(self, ooptree: OOPTree) -> None:
        """Set default values.

        Args:
            ooptree: the tree to print.
        """
        self._class_tree = ooptree

    def _add_to_tree(self, ooptree: OOPTree, tree: Tree | None = None) -> Tree:
        """Add a tree to a tree.

        Args:
            ooptree: the OOPTree object to use.
            tree: the Tree object to append to (if any).

        Returns:
            A newly created Tree object.
        """
        title = f'{ooptree.class_name}'
        if not tree:
            base_names = ''
            if ooptree.class_name_parents:
                base_names = ' (' + ', '.join(ooptree.class_name_parents) + ')'
            title = f'{ooptree.class_name}{base_names}'

        new_tree = Tree(title)
        for child in ooptree.children:
            self._add_to_tree(child, new_tree)

        if tree:
            tree.add(new_tree)

        return new_tree

    def print_to_console(self, console: Console) -> None:
        """Print the tree to the console.

        Args:
            console: a Rich console to print too.
        """
        t = self._add_to_tree(self._class_tree)
        console.print(t)
