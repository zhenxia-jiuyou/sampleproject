"""Example module with docstrings.

This is a module that shows all four types of docstrings:
- module docstring
- functions docstring
- class docstring
- method docstring
"""

class DocumentedClass:
    """Class that showcases method documentation.
    """

    def __init__(self):
        """Initialize class instance.
        Interesting note: docstrings are valid statements.
        It meands that if function or method doesn't have to
        do nothing and has docstring it doesn't have to feature
        any other statements.

        such no-op functions are useful for defining abstract
        methods or providing implementation stubs that have to be
        implemented later.
        """


def show_module_documentation():
    """Prints module documentation.

    Module documentation is available as global __doc__
    attribute. This attribute can be accessed and modified
    at any time.
    """
    print(__doc__)


