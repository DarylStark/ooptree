# OOPTree

The `OOPTree` Python library provides a convenient way to display a class hierarchy from either the command line, or interactively in a Python script. The user can use this, for instance, to see the class hierarchy of `Exceptions` to find a common base class to catch multiple exceptions or to gain insight into a library.

## Installation

Installation of the library is done using `pip`:

```bash
pip install ooptree
```

## Using `OOPTree` interactively

To use `ooptree` interactively in a Python REPL, you start the function `print_tree` and give it a class. For example:

```python
~ $ python
>>> from ooptree import print_tree
>>> print_tree(OSError)
OSError (Exception)
├── ConnectionError
│   ├── BrokenPipeError
│   ├── ConnectionAbortedError
│   ├── ConnectionRefusedError
│   └── ConnectionResetError
├── BlockingIOError
├── ChildProcessError
├── FileExistsError
├── FileNotFoundError
├── IsADirectoryError
├── NotADirectoryError
├── InterruptedError
├── PermissionError
├── ProcessLookupError
├── TimeoutError
├── UnsupportedOperation
└── itimer_error
```

This will print the tree for the `OSError` exception.

## Using it as a CLI script

You can also invoke the tree by using the `ooptree` command directly from your CLI. The CLI script has the following syntax:

```bash
ooptree [--module <module> ...] <classname>
```

You can specify what modules to include by using `--module`. This is needed when the wanted tree is in a module. For example:

```bash
~ $ ooptree --module rich.table JupyterMixin
JupyterMixin
├── Constrain
├── Align
├── VerticalCenter
├── Emoji
├── Text
├── Pretty
├── Padding
├── Panel
├── Table
├── Tree
├── Columns
├── Rule
├── Syntax
└── Markdown
```