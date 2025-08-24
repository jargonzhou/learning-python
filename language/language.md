# Python Programming Language
* https://docs.python.org/3/reference/index.html

# Lexical analysis
- Line structure
- Other tokens
- Identifiers and keywords
- Literals
- Operators
- Delimiters


# Data model
## Objects, values and types
## The standard type hierarchy

- 3.2.1. None
- 3.2.2. NotImplemented
- 3.2.3. Ellipsis `...` - [ref](https://realpython.com/python-ellipsis/)
- 3.2.4. `numbers.Number`
    - 3.2.4.1. `numbers.Integral`
    - 3.2.4.2. `numbers.Real` (`float`)
    - 3.2.4.3. `numbers.Complex` (`complex`)
- 3.2.5. Sequences
    - 3.2.5.1. Immutable sequences
    - 3.2.5.2. Mutable sequences
- 3.2.6. Set types
- 3.2.7. Mappings
    - 3.2.7.1. Dictionaries
- 3.2.8. Callable types
    - 3.2.8.1. User-defined functions
    - 3.2.8.2. Instance methods
    - 3.2.8.3. Generator functions
    - 3.2.8.4. Coroutine functions
    - 3.2.8.5. Asynchronous generator functions
    - 3.2.8.6. Built-in functions
    - 3.2.8.7. Built-in methods
    - 3.2.8.8. Classes
    - 3.2.8.9. Class Instances
- 3.2.9. Modules
- 3.2.10. Custom classes
- 3.2.11. Class instances
- 3.2.12. I/O objects (also known as file objects)
- 3.2.13. Internal types
    - 3.2.13.1. Code objects
    - 3.2.13.2. Frame objects
    - 3.2.13.3. Traceback objects
    - 3.2.13.4. Slice objects
    - 3.2.13.5. Static method objects
    - 3.2.13.6. Class method objects

## Special method names

- 3.3.1. Basic customization
- 3.3.2. Customizing attribute access
    - 3.3.2.1. Customizing module attribute access
    - 3.3.2.2. Implementing Descriptors
    - 3.3.2.3. Invoking Descriptors
    - 3.3.2.4. `__slots__`
- 3.3.3. Customizing class creation
    - 3.3.3.1. Metaclasses
    - 3.3.3.2. Resolving MRO entries
    - 3.3.3.3. Determining the appropriate metaclass
    - 3.3.3.4. Preparing the class namespace
    - 3.3.3.5. Executing the class body
    - 3.3.3.6. Creating the class object
    - 3.3.3.7. Uses for metaclasses
- 3.3.4. Customizing instance and subclass checks
- 3.3.5. Emulating generic types
    - 3.3.5.1. The purpose of `___class_getitem___`
    - 3.3.5.2. `___class_getitem___` versus `___getitem___`
- 3.3.6. Emulating callable objects
- 3.3.7. Emulating container types
- 3.3.8. Emulating numeric types
- 3.3.9. With Statement Context Managers
- 3.3.10. Customizing positional arguments in class pattern matching
- 3.3.11. Emulating buffer types
- 3.3.12. Special method lookup


特殊方法:

| Category                          | Method names                                                      |
| --------------------------------- | ----------------------------------------------------------------- |
| String/bytes representation       | `__repr__ __str__ __format__ __bytes__ __fspath__`                |
| Conversion to number              | `__bool__ __complex__ __int__ __float__ __hash__ __index__`       |
| Emulating collections             | `__len__ __getitem__ __setitem__ __delitem__ __contains__`        |
| Iteration                         | `__iter__ __aiter__ __next__ __anext__ __reversed__`              |
| Callable or coroutine execution   | `__call__ __await__`                                              |
| Context management                | `__enter__ __exit__ __aexit__ __aenter__`                         |
| Instance creation and destruction | `__new__ __init__ __del__`                                        |
| Attribute management              | `__getattr__ __getattribute__ __setattr__ __delattr__ __dir__`    |
| Attribute descriptors             | `__get__ __set__ __delete__ __set_name__`                         |
| Abstract base classes             | `__instancecheck__ __subclasscheck__`                             |
| Class metaprogramming             | `__prepare__ __init_subclass__ __class_getitem__ __mro_entries__` |

操作符特殊方法:

| Operator category               | Symbols                                      | Method names                                                                                        |
| ------------------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Unary numeric                   | `- + abs()`                                  | `__neg__ __pos__ __abs__`                                                                           |
| Rich comparison                 | `< <= == != > >=`                            | `__lt__ __le__ __eq__ __ne____gt__ __ge__`                                                          |
| Arithmetic                      | `+ - * / // % @ divmod() round() ** pow()`   | `__add__ __sub__ __mul__ __truediv__ __floordiv__ __mod__ __matmul__ __div mod__ __round__ __pow__` |
| Reversed arithmetic             | (arithmetic operators with swapped operands) | `__radd__ __rsub__ __rmul__ __rtrue div__ __rfloordiv__ __rmod__ __rmat mul__ __rdivmod__ __rpow__` |
| Augmented assignment arithmetic | `+= -= *= /= //= %= @= **=`                  | `__iadd__ __isub__ __imul__ __itrue div__ __ifloordiv__ __imod__ __imat mul__ __ipow__`             |
| Bitwise                         | `& \| ^ << >> ~`                             | `__and__ __or__ __xor__ __lshift__ __rshift__ __invert__`                                           |
| Reversed bitwise                | (bitwise operators with swapped operands)    | `__rand__ __ror__ __rxor__ __rlshift__ __rrshift__`                                                 |


# Coroutines
- 3.4.1. Awaitable Objects
  - `__await__()`
- 3.4.2. Coroutine Objects
  - `send()`
  - `throw()`
  - `close()`
- 3.4.3. Asynchronous Iterators
  - `__aiter__()`
  - `__anext__()`
- 3.4.4. Asynchronous Context Managers
  - `__aenter__()`
  - `__aexit__()`


# Execution model
- Structure of a program
- Naming and binding
- Exceptions

# The import system
- `importlib`
- Packages
- Searching
- Loading
- The Path Based Finder
- Replacing the standard import system
- Package Relative Imports
- Special considerations for __main__
- References

# Expressions
- Arithmetic conversions
- Atoms
- Primaries
- Await expression
- The power operator
- Unary arithmetic and bitwise operations
- Binary arithmetic operations
- Shifting operations
- Binary bitwise operations
- Comparisons
- Boolean operations
- Assignment expressions
- Conditional expressions
- Lambdas
- Expression lists
- Evaluation order
- Operator precedence

# Simple statements
- Expression statements
- Assignment statements
- The `assert` statement
- The `pass` statement
- The `del` statement
- The `return` statement
- The `yield` statement
- The `raise` statement
- The `break` statement
- The `continue` statement
- The `import` statement
- The `global` statement
- The `nonlocal` statement
- The `type` statement

# Compound statements
- The `if` statement
- The `while` statement
- The `for` statement
- The `try` statement
- The `with` statement
- The `match` statement
- Function definitions
- Class definitions
- Coroutines
- Type parameter lists

# Top-level components
- Complete Python programs
- File input
- Interactive input
- Expression input

# Full Grammar specification



# Implementations

### CPython
* https://github.com/python/cpython

> CPython is the reference implementation of Python. It is written in C, meeting the C89 standard (Python 3.11 uses C11) with several select C99 features.

[Stackless Python](https://github.com/stackless-dev/stackless/wiki/): microthreads, channels, scheduling
- archived 2025-02-13

### Cython
* https://cython.org/

> Cython is an optimising static compiler for both the Python programming language and the extended Cython programming language (based on Pyrex). It makes writing C extensions for Python as easy as Python itself.

### Jython
* https://www.jython.org/

> The Jython project provides implementations of Python in Java, providing to Python the benefits of running on the JVM and access to classes written in Java. The current release (a Jython 2.7.x) only supports Python 2 (sorry). There is work towards a Python 3 in the project’s GitHub repository.
> - [Story of Jython](http://hugunin.net/story_of_jython.html)

### PyPy
* https://pypy.org/

> A fast, compliant alternative implementation of Python

<!--
### Mojo
* https://www.modular.com/mojo

> Mojo is a pythonic language for blazing-fast CPU+GPU execution without CUDA. Optionally use it with MAX for insanely fast AI inference.

-->

# Modules, Packages
* [The Python Tutorial - Modules](https://docs.python.org/3/tutorial/modules.html)
* [Python Module Index](https://docs.python.org/3/py-modindex.html)

example: 

* [[Relative imports for the billionth time|https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time]]
* [[Relative Imports in Python 3|https://sparkbyexamples.com/python/relative-imports-in-python-3/]]

```shell
$ tree Myproject
Myproject/
├── main.py
├── package1/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── package2/
    ├── __init__.py
    ├── module3.py
    └── module4.py

### (1) Relative Import Module from the Same Package
# module1.py
from ..package_2 import module3
# module1.py
from module2 import print_hi
print_hi()
# Absolute import
# module1.py
from Package_1.module2 import print_hi

# erros: "ImportError: attempted relative import with no known parent package"
# This error occurs because they execute the file as a python script and not as a python module.
# Run the code on Terminal
python -m Package.module

### (2) Relative Import Module from Different Packages
# module1.py
from ..package_2 import module3
# module1.py
from ..package_2.module3 import bar

### (3) Relative Import from Sub Module
Myproject/
├── main.py
└── package1/
    ├── __init__.py
    ├── module1a.py
    ├── module1b.py
    └── subpackage/
        ├── __init__.py
        └── module1c.py
# module1c.py
from .. import module1a
```

# More
* [The Python Wiki](https://wiki.python.org/moin/)