# Python Programming Language

## Implementations

### CPython
* https://github.com/python/cpython

> CPython is the reference implementation of Python. It is written in C, meeting the C89 standard (Python 3.11 uses C11) with several select C99 features.

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

## Modules, Packages
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

## PEP: Python Enhancement Proposals
* [PEP 0 – Index of Python Enhancement Proposals (PEPs)](https://peps.python.org/pep-0000/)
- PEP 8 – Style Guide for Python Code
- PEP 249 – Python Database API Specification v2.0
- PEP 484 – Type Hints
- PEP 557 – Data Classes - `@dataclass`
- PEP 3333 – Python Web Server Gateway Interface v1.0.1
  - [WSGI (Web Server Gateway Interface)](https://wsgi.readthedocs.io/)
  - [ASGI (Asynchronous Server Gateway Interface)](https://asgi.readthedocs.io/)

type key:

* I: Informational
* P: Process
* S: Standards Track

status key:

* A: Accepted
* A: Active
* D: Deferred
* `<No letter>`: Draft
* F: Final
* P: Provisional
* R: Rejected
* S: Superseded
* W: Withdraw