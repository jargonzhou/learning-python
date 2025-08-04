# Introducing Python

| #   | Title                                             | Progress | Description |
| :-- | :------------------------------------------------ | :------- | :---------- |
| 1   | [[#5.1 A Taste of Py]]                            | %     |   |
| 2   | [[#5.2 Data Types, Values, Variables, and Names]] | %     |   |
| 3   | [[#5.3 Numbers]]                                  | %     |   |
| 4   | [[#5.4 Choose with if]]                           | %     |   |
| 5   | [[#5.5 Text Strings]]                             | %     |   |
| 6   | [[#5.6 Loop with while and for]]                  | %     |   |
| 7   | [[#5.7 Tuples and Lists]]                         | %     |   |
| 8   | [[#5.8 Dictionaries and Sets]]                    | %     |   |
| 9   | [[#5.9 Functions]]                                | %     |   |
| 10  | [[#5.10 Oh Oh Objects and Classes]]               | %     |   |
| 11  | [[#5.11 Modules, Packages, and Goodies]]          | 100%     | 2024-08-12  |
| 12  | [[#5.12 Wrangle and Mangle Data]]                 | %     |   |
| 13  | [[#5.13 Calendars and Clocks]]                    | %     |   |
| 14  | [[#5.14 Files and Directories]]                   | %     |   |
| 15  | [[#5.15 Data in Time Processes and Concurrency]]  | %     |   |
| 16  | [[#5.16 Data in a Box Persistent Storage]]        | %     |   |
| 17  | [[#5.17 Data in Space Networks]]                  | %     |   |
| 18  | [[#5.18 The Web, Untangled]]                      | %     |   |
| 19  | [[#5.19 Be a Pythonista]]                         | %     |   |
| 20  | [[#5.20 Py Art]]                                  | %     |   |
| 21  | [[#5.21 Py at Work]]                              | %     |   |
| 22  | [[#5.22 Py Sci]]                                  | %     |   |

# 1 Tips for Recapture

<!-- 帮助重温的过程总结. -->

1. Modern Computing in Simple Packages


# 2 术语

<!-- 记录阅读过程中出现的关键字及其简单的解释. -->

<!-- 进展中需要再次确认的术语:

进行中: 术语1
已完成: ~~术语1~~
-->
- Pythonic: In short, “pythonic” describes a coding style that leverages Python’s unique features to write code that is readable and beautiful. 
- Pythonista: someone who use the Python programming language. - [wikipedia](https://en.wiktionary.org/wiki/Pythonista)
# 3 介绍

<!-- 描述书籍阐述观点的来源、拟解决的关键性问题和采用的方法论等. -->

# 4 动机

<!-- 描述阅读书籍的动机, 要达到什么目的等. -->

# 5 概念结构

<!-- 描述书籍的行文结构, 核心主题和子主题的内容结构和关系. -->
- I. Python Basics: 1-11
- II. Python in Practice: 12-22

## 5.1 A Taste of Py

modules:
- `webbrowser`
- `json`
- `urllib.request`
- `requests`

The Zen of Python, by Tim Peters
## 5.2 Data: Types, Values, Variables, and Names

Python object:
- type
- id
- value
- reference count

Types:
- `bool`: `True`, `False` - [[#5.3 Numbers]]
- `int`: `42` - [[#5.3 Numbers]]
- `float`: `3.14` - [[#5.3 Numbers]]
- `complex`: `3 + 4j` - [[#5.22 Py Sci]]
- `str`: `'alas'`, `"alas"`, `'''alas'''`, '"""alas"""' - [[#5.5 Text Strings]]
- `list`: `[1, 2, 3]` - [[#5.7 Tuples and Lists]]
- `tuple`: `(2, 4, 8)` - [[#5.7 Tuples and Lists]]
- `bytes`: `b'ab\xff'` - [[#5.12 Wrangle and Mangle Data]]
- `bytearray`: `bytearray(...)` - [[#5.12 Wrangle and Mangle Data]]
- `set`: `set([3, 5, 7])` - [[#5.8 Dictionaries and Sets]]
- `frozenset`: `frozenset(['Elsa', 'Otto'])` - [[#5.8 Dictionaries and Sets]]
- `dict`: `{'game': 'bingo', 'dog': 'dingo'}` - [[#5.8 Dictionaries and Sets]]

```python
help("keywords")

import keyword
keyword.kwlist
```

Variables are names, not places.

## 5.3 Numbers

- booleans
- integers
- floats

math functions: [[#5.22 Py Sci]]

## 5.4 Choose with if

`#`: comment
`\`: continue lines

false values:
- `False`
- `None`
- `0`
- `0.0`
- `''`
- `[]`
- `()`
- `{}`
- `set()`

walrus operator: `name := expression` (Python 3.8)

`for`, `while`: [[#5.6 Loop with while and for]]
## 5.5 Text Strings

## 5.6 Loop with while and for
## 5.7 Tuples and Lists
## 5.8 Dictionaries and Sets
## 5.9 Functions
## 5.10 Oh Oh: Objects and Classes

> [!info] What Are Objects?

> [!info] Simple Objects

> [!info] Inheritance

> [!info] In `self` Defense

> [!info] Attribute Access

> [!info] Method Types

> [!info] Duck Typing

> [!info] Magic Methods

Table 10-1. Magic methods for comparison
- `__eq__`, `__ne__`, `__lt__`, `__gt__`, `__le__`, `__ge__`

Table 10-2. Magic methods for math
- `__add__`, `__sub__`, `__mul__`, `__floordiv__`, `__truediv__`, `__mod__`, `__pow__`
Table 10-3. Other, miscellaneous magic methods
- `__str__`, `__repr__`, `__len__`

> [!info] Aggregation and Composition

> [!info] When to Use Objects or Something Else

> [!info] Named Tuples

> [!info] Dataclasses

> [!info] Attrs

## 5.11 Modules, Packages, and Goodies
> [!info] Modules and the `import` Statement
```python
import fast
import fast as f

from fast import pick
from fast import pick as who_cares
```
> [!info] Packages

packages: organize modules into file and module hierarchies
```python
# questions.py
from choices import fast, advice

# choices/fast.py

# choices/advice.py
```

> The Modules Search Path
```python
import sys
print(sys.path)

sys.path.insert(0, "/my/modules")
```

> Relative and Absolute Imports
```python
import rougarou

# rougarou.py in the same directory
from . import rougarou

# rougarou.py in the directory above
from .. import rougarou

# rougarou.py under a slibing directory called creatures
from ..creatures import rougarou
```

> Namespace Packages

package modules as: 
- a single module(`.py` file)
- a package (directory containing modules, and possibly other packages).
```python
# critters
# |- rougarou.py
# |- wendigo.py
from critters import wendigo, rougarou

# namespace packges: spilt a package acroos directories
# north
# |- critters
# |-|- wendigo.py
# source
# |- critters
# |- rougarou.py

# put north and south in module search path
from critters import wendigo, rougarou
```

> Modules Versus Objects

- all the classes, functions, and global variables in a module are available to the outside.
- objects can use properties and `__` naming to hide or control access to their data attribtues.

> [!info] Goodies in the Python Standard Library

> Handling Missing Keys with `setdefault()` and `defaultdict()`
```python
periodic_table = {'Hydrogen': 1, 'Helium': 2}
carbon = periodic_table.setdefault('Carbon', 12)

from collections import defaultdict
# int, list, dict
periodic_table = defaultdict(int)
```

> Count Items with `Counter`
```python
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)

# +, -, &, |
breakfast_counter + lunch_counter
```

> Order by Key with `OrderedDict()`
```python
from collections import OrderedDict
```

> Stack + Queue == deque
```python
from collections import deque
```

> Iterate over Code Structure with `itertools`
```python
import itertools
# chain, cycle, accumulate
```

> Print Nicely with `pprint()`
```python
from pprint import pprint
```

> Get Random
```python
from random import choice
from random import sample
from random import randint
from random import randrange
from random import random
```

> [!info] More Batteries: Get Other Python Code

- [PyPI](https://pypi.org/): the Python Package Index
- GitHub
- [Read the Docs](https://about.readthedocs.com/): Sphinx, MkDocs, Jupyter Book
- [ActiveState Code - Popular Python Recipes](https://code.activestate.com/recipes/langs/python/)

## 5.12 Wrangle and Mangle Data
## 5.13 Calendars and Clocks
## 5.14 Files and Directories
## 5.15 Data in Time: Processes and Concurrency
## 5.16 Data in a Box: Persistent Storage
## 5.17 Data in Space: Networks
## 5.18 The Web, Untangled
## 5.19 Be a Pythonista
## 5.20 Py Art
## 5.21 Py at Work
## 5.22 Py Sci

# 6 总结

<!-- 概要记录书籍中如何解决关键性问题的. -->

# 7 应用

<!-- 记录如何使用书籍中方法论解决你自己的问题. -->

# 8 文献引用

<!-- 记录相关的和进一步阅读资料: 文献、网页链接等. -->

# 9 其他备注
