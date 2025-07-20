# pycodestyle
* https://github.com/pycqa/pycodestyle

> pycodestyle is a tool to check your Python code against some of the style conventions in PEP 8.


## Comments

### Functions, Methods

A function must have a docstring, unless it meets all of the following criteria:
not externally visible
very short
obvious

A docstring should give enough information to write a call to the function without reading the function's code.
A docstring should describe the function's calling syntax and its semantics, not its implementation.
For tricky code, comments alongside the code are more appropriate than using docstrings.

Certain aspects of a function should be documented in special sections, listed below.
Each section begins with a heading line, which ends with a colon.
Sections should be indented two spaces, except for the heading.

(1) Arguments

Args:
List each parameter by name. A description should follow the name, and be separated by a colon and a space.
If the description is too long to fit on a single 80-character line, use a hanging indent of 2 or 4 spaces (be consistent with the rest of the file).
The description should mention required type(s) and the meaning of the argument.

If a function accepts `*foo` (variable length argument lists) and/or `**bar` (arbitrary keyword arguments), they should be listed as `*foo` and `**bar`.

(2) Return Values

Returns: (or Yields: for generators)
Describe the type and semantics of the return value. If the function only returns None, this section is not required.

(3) Exceptions

Raises:
List all exceptions that are relevant to the interface.

```python
def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
    """Fetches rows from a Bigtable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
        big_table: An open Bigtable Table instance.
        keys: A sequence of strings representing the key of each table row
            to fetch.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {'Serak': ('Rigel VII', 'Preparer'),
         'Zim': ('Irk', 'Invader'),
         'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
    pass
```

### Classes

Classes should have a doc string below the class definition describing the class.

(1) Attributes

If your class has public attributes, they should be documented here in an Attributes section and follow the same formatting as a function's Args section.

```python
class SampleClass(object):
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""
```

!! Blocks, Inline

Complicated operations get a few lines of comments before the operations commence.

Non-obvious ones get comments at the end of the line.

```python
# 4 We use a weighted dictionary search to find out where i is in
# 5 the array.  We extrapolate position based on the largest num
# 6 in the array and the array size and then do binary search to
# 7 get the exact number.

if i & (i-1) == 0:        # true iff i is a power of 2
```
