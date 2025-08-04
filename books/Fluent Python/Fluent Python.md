# Fluent Python

| #   | Title                                                   | Progress | Description |
| :-- | :------------------------------------------------------ | :------- | :---------- |
| 1   | [[#5.1 The Python Data Model]]                          | 100%     | 2024-11-04  |
| 2   | [[#5.2 An Array of Sequences]]                          | 100%     | 2024-11-05  |
| 3   | [[#5.3 Dictionaries and Sets]]                          | 100%     | 2024-11-05  |
| 4   | [[#5.4 Unicode Text Versus Bytes]]                      | %        |             |
| 5   | [[#5.5 Data Class Builders]]                            | 100%     | 2024-11-05  |
| 6   | [[#5.6 Object References, Mutability, and Recycling]]   | 100%     | 2024-11-06  |
| 7   | [[#5.7 Functions as First-Class Objects]]               | 100%     | 2024-11-06  |
| 8   | [[#5.8 Type Hints in Functions]]                        | 100%     | 2024-11-07  |
| 9   | [[#5.9 Decorators and Closures]]                        | 100%     | 2024-11-07  |
| 10  | [[#5.10 Design Patterns with First-Class Functions]]    | %        |             |
| 11  | [[#5.11 A Pythonic Object]]                             | 100%     | 2024-11-07  |
| 12  | [[#5.12 Special Methods for Sequences]]                 | %        |             |
| 13  | [[#5.13 Interfaces, Protocols, and ABCs]]               | %        |             |
| 14  | [[#5.14 Inheritance For Better or for Worse]]           | %        |             |
| 15  | [[#5.15 More About Type Hints]]                         | %        |             |
| 16  | [[#5.16 Operator Overloading]]                          | 100%     | 2024-11-12  |
| 17  | [[#5.17 Iterators, Generators, and Classic Coroutines]] | 100%     | 2024-11-08  |
| 18  | [[#5.18 with, match, and else Blocks]]                  | 100%     | 2024-11-08  |
| 19  | [[#5.19 Concurrency Models in Python]]                  | 100%     | 2024-11-10  |
| 20  | [[#5.20 Concurrent Executors]]                          | 100%     | 2024-11-10  |
| 21  | [[#5.21 Asynchronous Programming]]                      | 100%     | 2024-11-10  |
| 22  | [[#5.22 Dynamic Attributes and Properties]]             | 100%     | 2024-11-11  |
| 23  | [[#5.23 Attribute Descriptors]]                         | 80%      | 2024-11-11  |
| 24  | [[#5.24 Class Metaprogramming]]                         | 80%      | 2024-11-11  |
|     |                                                         |          |             |
|     |                                                         |          |             |

# 1 Tips for Recapture

<!-- 帮助重温的过程总结. -->

1. Version: 3.10.
2. WARNING: the author is talktive, when reading, we should concertrate on the topic.

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
- 复习Python编程知识点.

# 5 概念结构

<!-- 描述书籍的行文结构, 核心主题和子主题的内容结构和关系. -->
- Part I. Data Structures: 1 - 6
- Part II. Functions as Objects: 7 - 10
- Part III. Classes and Protocols: 11 - 16
- Part IV. Control Flow: 17 - 21
- Part V. Metaprogramming: 22 - 24

## 5.1 The Python Data Model
special methods
```python
collections.namedtuple(...)

__init__
__len__      # len
__getitem__  # sequence indexing/slicing, iterable

random.choice(...)
in # sequence scan, __contains__
```

How Special Methods Are Used
```python
for i in x
	iter(x)
		x.__iter__()
		x.__getitem__()
```
- Emulating numeric types
example: two-dimensional vectors
```python
__repr__
__abs__
__add__
__mul__
```
- String representation of objects
```python
__repr__ # repr()
__str__  # str()
```
- Boolean value of an object
```python
bool(X)
	x.__bool__()
	x.__len__()
```
- Implementing collections
## 5.2 An Array of Sequences

Table 2-1. Methods and attributes found in list or tuple (methods implemented by object are omitted for brevity)

PEP 448—Additional Unpacking Generalizations: iterable unpacking

PEP 634—Structural Pattern Matching: Specification: `match/case` statement
## 5.3 Dictionaries and Sets

- dictcomp: dict comprehension 

PEP 448—Additional Unpacking Generalizations

`collections.abc.Mapping`

PEP 456—Secure and interchangeable hash algorithm

## 5.4 Unicode Text Versus Bytes
## 5.5 Data Class Builders
## 5.6 Object References, Mutability, and Recycling


## 5.7 Functions as First-Class Objects
## 5.8 Type Hints in Functions


PEP 544—Protocols: Structural subtyping (static duck typing): `Protocol`, similar to Go interface

`collections.abc.Callable`
```python
Callable[[ParamType1, ParamType2], ReturnType]
```

- [[#5.15 More About Type Hints]]
## 5.9 Decorators and Closures

PEP 318—Decorators for Functions and Methods

## 5.10 Design Patterns with First-Class Functions


## 5.11 A Pythonic Object

example: `Vector2d`

object representation:
```python
str()
repr()
__str__
__repr__
__bytes__
__format__
```

```python
__iter__
__eq__
__abs__
__bool__

@classmethod
```

- [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#formatspec)

```python
__hash__
@property
__match_args__
```

Example 11-11. vector2d_v3.py: the full monty

```python
__dict__
```
## 5.12 Special Methods for Sequences
## 5.13 Interfaces, Protocols, and ABCs
## 5.14 Inheritance: For Better or for Worse
## 5.15 More About Type Hints
## 5.16 Operator Overloading
- infix operators: `+`, `|`
- unary operators: `-`, `~`
- function invocation operator: `()`
- attribute access operator: `.`
- item access/slicing operator: `[]`


## 5.17 Iterators, Generators, and Classic Coroutines
the Iterator design pattern
## 5.18 with, match, and else Blocks

context manager interface:
```python
__enter__(self)
__exit__(self, exc_type, exc_value, traceback)
```
`contextlib`

- [Lispy: Scheme Interpreter in Python 3.10](https://github.com/fluentpython/example-code-2e/blob/master/18-with-match/lispy/py3.10/lis.py)

`else`:
- `if/else`
- `for/else`: when the `for` loop runs to completion
- `while/else`: when the `while` loop exits
- `try/else`: no exception is raised in the `try` block

## 5.19 Concurrency Models in Python
- `threading`
- `multiprocessing`
- `asyncio`

terms:
- concurrency
- parallelism
- execution unit
- process
- thread
- coroutine
- queue
- lock
- contention

GIL(Global Interpreter Lock)

`threading`:
```python
Thread
Event
Event.set()
Event.wait()
Event.wait(timeout)
```
`multiprocessing`:
```python
Process
Event
```
`asyncio`:
```python
run()
async def
create_task()
Task
await
Task.cancel()
CencelledError
sleep(timeout)
```

## 5.20 Concurrent Executors
`concurrent.futures.Executor`

futures:
```python
concurrent.futures.Future
asyncio.Future
```

- [tqdm](https://github.com/tqdm/tqdm): A Fast, Extensible Progress Bar for Python and CLI
## 5.21 Asynchronous Programming

Awaitable

- [HTTPX](https://www.python-httpx.org/): HTTPX is a fully featured HTTP client for Python 3, which provides sync and async APIs, and support for both HTTP/1.1 and HTTP/2.

Figure 21-1. In an asynchronous program, a user’s function starts the event loop, scheduling an initial coroutine with `asyncio.run`. Each user’s coroutine drives the next with an await expression, forming a channel that enables communication between a library like HTTPX and the event loop.

- [asyncpg](https://magicstack.github.io/asyncpg/current/): asyncpg is a database interface library designed specifically for PostgreSQL and Python/asyncio. asyncpg is an efficient, clean implementation of PostgreSQL server binary protocol for use with Python’s asyncio framework. asyncpg requires Python 3.8 or later and is supported for PostgreSQL versions 9.5 to 17. Other PostgreSQL versions or other databases implementing the PostgreSQL protocol may work, but are not being actively tested.

PEP 492—Coroutines with async and await syntax
```python
async with
__aenter__
__aexit__
```

```python
asyncio.to_thread() # Python 3.9
loop.run_in_executor() # Python 3.7, 3.8
asyncio.Semaphore
```

- [FastAPI](https://fastapi.tiangolo.com/): FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.
- [ASGI (Asynchronous Server Gateway Interface)](https://asgi.readthedocs.io/en/latest/index.html): ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI, intended to provide a standard interface between async-capable Python web servers, frameworks, and applications. Where WSGI provided a standard for synchronous Python apps, ASGI provides one for both asynchronous and synchronous apps, with a WSGI backwards-compatibility implementation and multiple servers and application frameworks.
	- implementation: uvicorn

```python
async for
__aiter__
__anext__

@asynccontextmanager
```

- [Curio](https://curio.readthedocs.io/en/latest/index.html): Curio is a coroutine-based library for concurrent Python systems programming. It provides standard programming abstractions such as as tasks, sockets, files, locks, and queues. You’ll find it to be familiar, small, fast, and fun.

## 5.22 Dynamic Attributes and Properties

```python
@property
__getattr__
```

```python
__class__
__dict__
__slots__

dir([object])
getattr(object, name[, default])
hasattr(object, name)
setattr(object, name, value)
vars([object])

__delattr__(self, name)
__dir__(self)
__getattr__(self, name)
__getattribute__(self, name)
__setattr__(self, name, value)
```

## 5.23 Attribute Descriptors

```python
__get__
__set__
__delete__
```

## 5.24 Class Metaprogramming

```python
__class__
__name__
__mro__ # method resolution order

cls.__bases__
cls.__qualname__
cls.__subclasses__()
cls.mro()
```

```python
type()
```

PEP 487—Simpler customization of class creation
```python
__init_subclass__
__set_name__
```


# 6 总结

<!-- 概要记录书籍中如何解决关键性问题的. -->

# 7 应用

<!-- 记录如何使用书籍中方法论解决你自己的问题. -->

# 8 文献引用

<!-- 记录相关的和进一步阅读资料: 文献、网页链接等. -->
- Luciano Ramalho. Fluent Python: Clear, Concise, and Effective Programming. O’Reilly Media: 2022. 
	- Companion site: https://www.fluentpython.com/
	- Code: https://github.com/fluentpython/example-code-2e

# 9 其他备注
- doctest
- pytest

- [The Python Tutorial](https://docs.python.org/3/tutorial/)
- The Python Language Reference