"""The main module for the CLI script."""

from typing import Annotated

import typer

from . import print_tree


def main(
    base_class_name: str,
    module: Annotated[
        list[str],
        typer.Option(default_factory=list, help='Import specific modules.'),
    ],
) -> None:
    """Print the class hierarchy for a specific class."""
    print_tree(base_class_name, module)


if __name__ == '__main__':
    typer.run(main)
