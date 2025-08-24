"""
Unit test of functions as first-class objects.

packages: functtools, operator
"""
# pylint: skip-file


import random
from typing import Any, Optional, Sequence, Union
import unittest
from functools import reduce
from operator import add


def factorial(n: int) -> int:
  """return n!"""
  return 1 if n < 2 else n * factorial(n - 1)


class TestFunction(unittest.TestCase):
  def test_function(self) -> None:
    self.assertEqual(1405006117752879898543142606244511569936384000000000,
                     factorial(42))
    self.assertEqual('return n!', factorial.__doc__)
    # self.assertTrue(isinstance(factorial, function))
    # self.assertEqual(type(factorial), function)
    print(type(factorial))

    # alias
    fact = factorial
    self.assertTrue(factorial is fact)
    self.assertListEqual([1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800],
                         list(map(fact, range(11))))

  def test_high_order_functions(self) -> None:
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    self.assertListEqual(['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry'],
                         sorted(fruits, key=len))

    # replacement for map, filter, reduce
    self.assertListEqual([1, 6, 120],
                         list(map(factorial, filter(lambda n: n % 2, range(6)))))
    # use listcomp
    self.assertListEqual([1, 6, 120],
                         [factorial(n) for n in range(6) if n % 2])

    self.assertEqual(sum(range(100)), reduce(add, range(100)))

    # all, any
    self.assertTrue(all([]))
    self.assertFalse(any([]))

  def test_anonymous_functions(self) -> None:
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    self.assertListEqual(['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry'],
                         sorted(fruits, key=lambda word: word[::-1]))

  def test_function_parameters(self) -> None:
    def tag(name: str, *content: str, class_: Optional[str] = None,
            **attrs: Union[str, int, Optional[str]]) -> str:
      """generate HTML tags

      Parameters
      ----------
      name: str
        tag name
      content: tuple[str]
        tag content
      class\_: str
        tag class
      attrs: dict
        tag attributes
      """
      if class_ is not None:
        attrs['class'] = class_
      attr_pairs = (f' {attr}="{value}"' for attr, value
                    in sorted(attrs.items()))
      attr_str = ''.join(attr_pairs)
      if content:
        elements = (f'<{name}{attr_str}>{c}</{name}>'
                    for c in content)
        return '\n'.join(elements)
      else:
        return f'<{name}{attr_str} />'

    # positional argument
    self.assertEqual('<br />', tag('br'))
    # *content as tuple
    self.assertEqual('<p>hello</p>', tag('p', 'hello'))
    self.assertEqual('<p>hello</p>\n<p>world</p>', tag('p', 'hello', 'world'))
    # **attrs as dict: id
    self.assertEqual('<p id="3">hello</p>', tag('p', 'hello', id=3))
    # keyword argument: _class
    self.assertEqual('<p class="sidebar">hello</p>\n<p class="sidebar">world</p>',
                     tag('p', 'hello', 'world', class_='sidebar'))
    # positional argument as keyword argument
    self.assertEqual('<img content="testing" />',
                     tag(content='testing', name="img"))
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
              'src': 'sunset.jpg', 'class': 'framed'}
    # **attrs
    self.assertEqual('<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />',
                     tag(**my_tag))

  def test_keyword_only_argument(self) -> None:
    # keyword only argument: after *
    def f(a: Any, *, b: Any) -> tuple[Any, Any]:
      return a, b
    self.assertTupleEqual((1, 2), f(1, b=2))
    # try:
    #   f(1, 2)
    # except TypeError as e:
    #   # takes 1 positional argument but 2 were given
    #   print(e)

  def test_positioal_only_argument(self) -> None:
    # positional only argument: before /
    def f(a: Any, b: Any, /) -> tuple[Any, Any]:
      return (a//b, a % b)
    self.assertTupleEqual((2, 2), f(10, 4))
    # try:
    #   f(10, b=4)
    # except TypeError as e:
    #   # got some positional-only arguments passed as keyword arguments: 'b'
    #   print(e)

  def test_partial_apply(self) -> None:
    """partial application"""
    from operator import mul
    from functools import partial
    triple = partial(mul, 3)
    print(type(triple))
    self.assertTrue(isinstance(triple, partial))
    self.assertEqual(6, triple(2))


class BingoCage:
  def __init__(self, items: Sequence[Any]) -> None:
    self._items = list(items)
    random.shuffle(self._items)

  def pick(self) -> Any:
    try:
      return self._items.pop()
    except IndexError:
      raise LookupError('pick from empty BingoCage')

  # __call__
  def __call__(self) -> Any:
    return self.pick()


class TestCallableObject(unittest.TestCase):
  """
  User-defined functions: def, lambda
  built-in functions: len, time.strftime
  built-in methods: dict.get
  methods
  classes: __new__, __init__
  class instances: __call__
  generator functions: yield
  native coroutine functions: async def
  asynchronous generator functions: async def + yield, async for
  """

  def test_user_defined_callable(self) -> None:
    bingo = BingoCage(range(3))
    self.assertIn(bingo.pick(), range(3))
    # callable
    self.assertTrue(callable(bingo))
