# Python in a Nutshell

| #   | Title                                                | Progress | Description |
| :-- | :--------------------------------------------------- | :------- | :---------- |
| 1   | [[#5.1 Introduction to Python]]                      | xxx%     | yyyy-mm-dd  |
| 2   | [[#5.2 The Python Interpreter]]                      | xxx%     | yyyy-mm-dd  |
| 3   | [[#5.3 The Python Language]]                         | xxx%     | yyyy-mm-dd  |
| 4   | [[#5.4 Object-Oriented Python]]                      | xxx%     | yyyy-mm-dd  |
| 5   | [[#5.5 Type Annotations]]                            | xxx%     | yyyy-mm-dd  |
| 6   | [[#5.6 Exceptions]]                                  | xxx%     | yyyy-mm-dd  |
| 7   | [[#5.7 Modules and Packages]]                        | 100%     | 2024-08-12  |
| 8   | [[#5.8 Core Built-ins and Standard Library Modules]] | xxx%     | yyyy-mm-dd  |
| 9   | [[#5.9 Strings and Things]]                          | xxx%     | yyyy-mm-dd  |
| 10  | [[#5.10 Regular Expressions]]                        | xxx%     | yyyy-mm-dd  |
| 11  | [[#5.11 File and Text Operations]]                   | xxx%     | yyyy-mm-dd  |
| 12  | [[#5.12 Persistence and Databases]]                  | xxx%     | yyyy-mm-dd  |
| 13  | [[#5.13 Time Operations]]                            | xxx%     | yyyy-mm-dd  |
| 14  | [[#5.14 Customizing Execution]]                      | xxx%     | yyyy-mm-dd  |
| 15  | [[#5.15 Concurrency Threads and Processes]]          | xxx%     | yyyy-mm-dd  |
| 16  | [[#5.16 Numeric Processing]]                         | xxx%     | yyyy-mm-dd  |
| 17  | [[#5.17 Testing, Debugging, and Optimizing]]         | xxx%     | yyyy-mm-dd  |
| 18  | [[#5.18 Networking Basics]]                          | xxx%     | yyyy-mm-dd  |
| 19  | [[#5.19 Client-Side Network Protocol Modules]]       | xxx%     | yyyy-mm-dd  |
| 20  | [[#5.20 Serving HTTP]]                               | xxx%     | yyyy-mm-dd  |
| 21  | [[#5.21 Email, MIME, and Other Network Encodings]]   | xxx%     | yyyy-mm-dd  |
| 22  | [[#5.22 Structured Text HTML]]                       | xxx%     | yyyy-mm-dd  |
| 23  | [[#5.23 Structured Text XML]]                        | xxx%     | yyyy-mm-dd  |
| 24  | [[#5.24 Packaging Programs and Extensions]]          | xxx%     | yyyy-mm-dd  |
| 25  | [[#5.25 Extending and Embedding Classic Python]]     | xxx%     | yyyy-mm-dd  |
| 26  | [[#5.26 v3.7 to v3.n Migration]]                     | xxx%     | yyyy-mm-dd  |

# 1 Tips for Recapture

<!-- 帮助重温的过程总结. -->

1. Step 1

# 2 术语

<!-- 记录阅读过程中出现的关键字及其简单的解释. -->

<!-- 进展中需要再次确认的术语:

进行中: 术语1
已完成: ~~术语1~~
-->

# 3 介绍

<!-- 描述书籍阐述观点的来源、拟解决的关键性问题和采用的方法论等. -->

# 4 动机

<!-- 描述阅读书籍的动机, 要达到什么目的等. -->

# 5 概念结构

<!-- 描述书籍的行文结构, 核心主题和子主题的内容结构和关系. -->
- Part I, Getting Started with Python: 1-2
- Part II, Core Python Language and Built-ins: 3-10
- Part III, Python Library and Extension Modules: 11-17
- Part IV, Network and Web Programming: 18-23
- Part V, Extending, Distributing, and Version Upgrade and Migration: 24-26

## 5.1 Introduction to Python
## 5.2 The Python Interpreter

> [!info] The `python` Program

> [!info] Python Development Environments

> [!info] Running Python Programs

> [!info] Running Python in the Browser

## 5.3 The Python Language

> [!info] Lexical Structure

> [!info] Data Types

> [!info] Variable and Other References

> [!info] Expressions and Operators

> [!info] Numeric Operations

> [!info] Sequence Operations

> [!info] Set Operations

> [!info] Dictionary Operations

> [!info] Control Flow Statements

> [!info] Functions

## 5.4 Object-Oriented Python

> [!info] Classes and Instances

> [!info] Special Methods

> [!info] Decorators

> [!info] Metaclasses

## 5.5 Type Annotations

> [!info] History

> [!info] Type-Checking Utilities

> [!info] Type Annotation Syntax

> [!info] The `typing` Module

> [!info] Using Type Annotations at Runtime

> [!info] How to Add Type Annotations to Your Cod

## 5.6 Exceptions

> [!info] The `try` Statement

> [!info] The `raise` Statement

> [!info] The `with` Statement and Context Managers

> [!info] Generators and Exceptions

> [!info] Exception Propagation

> [!info] Exception Objects

> [!info] Custom Exception Classes

> [!info] `ExceptionGroup` and `except*`

> [!info] Error-Checking Strategies

> [!info] The `assert` Statement

## 5.7 Modules and Packages
- [x] Python modules and packages

- module: each source file is a module.
- package: a hierarchical, tree-like structure of related modules and subpackages.
- `import`, `from`
- extension modules: modules coded in other languages(C, C++, Java, C#, Rust) see [[#5.25 Extending and Embedding Classic Python]]

> [!info] Module Objects

a module is an object with arbitrarily named attributes.
`sys.modules`

```python
import modname [as varname][,...]
```
- the module body
- attributes of module object
	- `__getattr__` function
	- `__dict__` attribute
	- `__name__` attribute
	- `__file__` attribute
- Python build-ins
	- preloaded module `builtins`
	- `__builtins__` attribute
- module documentation strings: `__doc__` attribute, see docstring in [[#5.3 The Python Language]]
- module-private variables
	- leading underscore `_` means private

```python
from modname import attrname [as varname][,...]
from modname import **
```
the `import` statement is often a better choice than the `from` statement.
- handling module failures: `ImportError`

> [!info] Module Loading
- `sys` module
- `__import__` function: check `sys.modules`

> Built-in Modules

`sys.builtin_module_names` tuple

> Searching the Filesystem for a Module

`sys.path`: `PYTHONPATH` environment variable
`*.pth` in `PYTHONHOME` directory

search the file for module M:
- `.pyd`, `.dll`, `.so`
- `.py`: source modules
	- `__pycache__/*.<tag>.pyc`
- `.pyc`: bytecode compiled modules
- `M/__init__.py`

> The Main Program

`if __name__ == '__main__':`

> Reloading Modules

`importlib.reload(M)`

> Circular Imports

Python lets you specify circular imports.
`sys.modules`

> Custom Importers

- rebinding `__import__`
- import hooks: PEP451, `sys.meta_path`, `sys.path_hooks`

> [!info] Packages

module body of package P is in file `P/__init__.py`
```python
import P.M
import P.M as V

from P import M
from P import M as V

from . import X
```

> Special Attributes of Package Objects
- `__file__`
- `__package__`
- `__all__` global variable in `P/__init__.py`: for `from P import *`
- `__path__`

> Absolute Versus Relative Imports
- absolute import: find in `sys.path`
- relative import: within current package
```python
from . import X
from .X import y
```


> [!info] Distribution Utilities (`distutils`) and `setuptools`

> [!info] Python Environments

## 5.8 Core Built-ins and Standard Library Modules

> [!info] Built-inTypes

> [!info] Built-in Functions

> [!info] The `sys` Module

> [!info] The `copy` Module

> [!info] The `collections` Module

> [!info] The `functools` Module

> [!info] The `heapq` Module

> [!info] The `argparse` Module

> [!info] The `itertools` Module

## 5.9 Strings and Things
> [!info] Methods of String Objects

> [!info] The `string` Module

> [!info] String Formatting

> [!info] Text Wrapping and Filling

> [!info] The `pprint` Module

> [!info] The `reprlib` Module

> [!info] Unicode

## 5.10 Regular Expressions

> [!info] Regular Expressions and the `re` Module

> [!info] Optional Flags

> [!info] Match Versus Search

> [!info] Anchoring at String Start and End

> [!info] Regular Expression Objects

> [!info] Match Objects

> [!info] Functions of the `re` Module

> [!info] REs and the `:=` Operator

> [!info] The Third-Party `regex` Module

## 5.11 File and Text Operations
## 5.12 Persistence and Databases
## 5.13 Time Operations
## 5.14 Customizing Execution
## 5.15 Concurrency: Threads and Processes
## 5.16 Numeric Processing
## 5.17 Testing, Debugging, and Optimizing

## 5.18 Networking Basics
## 5.19 Client-Side Network Protocol Modules
## 5.20 Serving HTTP
## 5.21 Email, MIME, and Other Network Encodings
## 5.22 Structured Text: HTML
## 5.23 Structured Text: XML

## 5.24 Packaging Programs and Extensions
## 5.25 Extending and Embedding Classic Python
## 5.26 v3.7 to v3.n Migration

## 5.27 Appendix. New Features and Changes in Python 3.7 Through 3.11


# 6 总结

<!-- 概要记录书籍中如何解决关键性问题的. -->

# 7 应用

<!-- 记录如何使用书籍中方法论解决你自己的问题. -->

# 8 文献引用

<!-- 记录相关的和进一步阅读资料: 文献、网页链接等. -->

# 9 其他备注
