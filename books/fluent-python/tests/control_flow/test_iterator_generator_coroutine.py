"""
Unit test of iterators, generators, classic coroutines.


classic coroutines
- Generator[YieldType, SendType, ReturnType]
  - YieldType: type of value returned by next(it)
  - SendType: relevant with coroutine, type of x in gen.send(x)
  - ReturnType: annotate a coroutine
"""
# pylint: skip-file


import unittest


class TestIterators(unittest.TestCase):
  pass


class TestGenerators(unittest.TestCase):

  def test_yield_from(self) -> None:
    # yield from: subgenerators
    from src.control_flow.generators import display
    display(BaseException)  # exception hierarchy


class TestClassicCoroutines(unittest.TestCase):
  def test_coroutine(self) -> None:
    # Gene
    pass
