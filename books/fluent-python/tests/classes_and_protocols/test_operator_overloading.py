"""
Unit test of operator overloading.

operator overloading 101
- infix operators: +, |
- unary operators: -, ~
- function invocation: ()
- attribute access: .
- item access/slicing: []

unary operators
- `-`: __neg__
- `+`: __pos__
- `~`: __invert__, bitwise inverse of an integer, ~x = -(x+1)
- `abs()`: __abs__

overloading + for Vector addition
- __add__

overloading * fro scalra multiplication
- __mul__

use @ as an infix operator
- __matmul__

wrap-up arithmetic operators
- Table 16-1. Infix operator method names

comparasion operators
- __eq__, __ne__, __gt__, __lt__, __ge__, __le__

augmented assignment operators
"""
# pylint: skip-file


import unittest


class TestOperatorOverloading(unittest.TestCase):
  def test_vector(self) -> None:
    from src.classes_and_protocols.vector import Vector
    from src.classes_and_protocols.vector2d import Vector2d

    # _add__
    v1 = Vector([3, 4, 5])
    self.assertEqual(Vector([13.0, 24.0, 35.0]), v1 + [10, 20, 30])
    v2d = Vector2d(1, 2)
    self.assertEqual(Vector([4.0, 6.0, 5.0]), v1 + v2d)

    # __radd__
    self.assertEqual(Vector([13, 24, 35]), (10, 20, 30) + v1)

    with self.assertRaises(TypeError) as cm:
      v1 + 1
      v1 + 'ABC'

    # __mul__, __rmul__
    self.assertEqual(Vector([30.0, 40.0, 50.0]), v1 * 10)
    self.assertEqual(Vector([33.0, 44.0, 55.0]), 11 * v1)
    from fractions import Fraction
    self.assertEqual(Vector([1.5, 2.0, 2.5]), v1 * Fraction(1, 2))

    # @: __matmul__, __rmatmul__, __imatmul__
    va = Vector([1, 2, 3])
    vz = Vector([5, 6, 7])
    self.assertEqual(38.0, va @ vz)
    self.assertEqual(380.0, [10, 20, 30] @ vz)

    with self.assertRaises(TypeError) as cm:
      va @ 3
    self.assertEqual("unsupported operand type(s) for @: 'Vector' and 'int'",
                     str(cm.exception))

    # ==: __eq__
    self.assertTrue(Vector([1, 2]) == Vector2d(1, 2))
    self.assertTrue(Vector([1, 2, 3]) != (1, 2, 3))

    # +=, *=
    v1 = Vector([1, 2, 3])
    v1 += Vector([4, 5, 6])
    self.assertEqual(Vector([5.0, 7.0, 9.0]), v1)
    v1 *= 11
    self.assertEqual(Vector([55.0, 77.0, 99.0]), v1)
