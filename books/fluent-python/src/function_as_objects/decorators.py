"""
Decorators


in std:
functools.cache
functools.lru_cache
functools.singledispatch
"""


import functools
import time
from typing import Any, Callable, Union


def deco(_func: Callable[..., None]) -> Callable[..., None]:
  """a decorator replace a function with another one"""
  def inner() -> None:
    print('running inner()')
  return inner


@deco
def target() -> None:
  """a decorated function"""
  print('running target()')


# registration: decorators run right after the decorated function is defined,
# ie at import time
registry: list[Callable[..., None]] = []


def register(func: Callable[..., None]) -> Callable[..., None]:
  """register decorator"""
  print(f'running register({func.__name__})')
  registry.append(func)
  return func


class Averager():
  """avg"""

  def __init__(self) -> None:
    self.series: list[float] = []

  def __call__(self, new_value: Union[float, int]) -> float:
    self.series.append(new_value)
    total = sum(self.series)
    return total / len(self.series)


def make_averager() -> Callable[[Union[float, int]], float]:
  """avg with closure"""
  series: list[float] = []

  def average(new_value: Union[float, int]) -> float:
    series.append(new_value)
    total = sum(series)
    return total / len(series)

  return average


def make_averager2() -> Callable[[Union[float, int]], float]:
  """avg with closure"""
  count: int = 0
  total: float = 0

  def average(new_value: Union[float, int]) -> float:
    # UnboundLocalError: cannot access local variable 'count'
    #   where it is not associated with a value
    # count += 1
    # total += new_value
    nonlocal count, total
    count += 1
    total += new_value

    return total / count

  return average


def clock(func: Callable[..., Any]) -> Any:
  """a timing decorator"""
  def clocked(*args: Any) -> Any:
    t0 = time.perf_counter()
    result = func(*args)
    elapsed = time.perf_counter() - t0
    name = func.__name__
    arg_str = ', '.join(repr(arg) for arg in args)
    print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
    return result
  return clocked


def clock2(func: Callable[..., Any]) -> Any:
  """a timing decorator with functools.wraps"""

  @functools.wraps(func)
  def clocked(*args: Any, **kwargs: Any) -> Any:  # also handle keyword arguments
    t0 = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - t0
    name = func.__name__
    arg_str = ', '.join(repr(arg) for arg in args)
    print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
    return result

  return clocked


DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({arg_str}) -> {result}'


def clock_p(fmt: str = DEFAULT_FMT) -> Any:
  """a parameterized timing decorator"""
  def decorate(func: Callable[..., Any]) -> Callable[..., Any]:
    def clocked(*args: Any) -> Any:
      t0 = time.perf_counter()
      _result = func(*args)
      # pylint: disable=possibly-unused-variable
      elapsed = time.perf_counter() - t0
      name = func.__name__
      arg_str = ', '.join(repr(arg) for arg in args)
      result = repr(_result)
      # locals(): local variables
      print(fmt.format(**locals()))
      return _result
    return clocked
  return decorate


# pylint: disable=invalid-name
class clock_c:
  """a class based timming decorator"""

  def __init__(self, fmt: str = DEFAULT_FMT) -> None:
    self.fmt = fmt

  def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
    def clocked(*_args: Any) -> Any:
      t0 = time.perf_counter()
      _result = func(*_args)
      # pylint: disable=possibly-unused-variable
      elapsed = time.perf_counter() - t0
      name = func.__name__
      arg_str = ', '.join(repr(arg) for arg in _args)
      result = repr(_result)
      print(self.fmt.format(**locals()))
      return _result
    return clocked


# decorator factory
registry_set: set[Callable[..., Any]] = set()


def register_f(active: bool = True) -> Callable[..., Any]:
  """a parameterized decorator"""
  def decorate(func: Callable[..., Any]) -> Callable[..., Any]:
    print('running register factory', f'(active={active}->decorate{func}')
    if active:
      registry_set.add(func)
    else:
      registry_set.discard(func)
    return func
  return decorate
