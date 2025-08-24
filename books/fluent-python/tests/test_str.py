"""
Example of unittest.

https://docs.python.org/3/library/unittest.html
"""
import unittest

# pylint: disable=missing-class-docstring,missing-function-docstring


class TestStringMethods(unittest.TestCase):
  def test_upper(self) -> None:
    self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self) -> None:
    self.assertTrue('FOO'.isupper())
    self.assertFalse('Foo'.isupper())

  def test_split(self) -> None:
    s = 'hello world'
    self.assertEqual(s.split(), ['hello', 'world'])
    # check that s.split fails when the separator is not a string
    with self.assertRaises(TypeError) as cm:
      s.split(2)
    self.assertEqual("must be str or None, not int",
                     str(cm.exception))


if __name__ == '__main__':
  unittest.main()
