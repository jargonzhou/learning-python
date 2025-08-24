"""
Unit test of Vector.
"""

from src.data_structures.vector2d import Vector
import unittest

# pylint: skip-file


class TestVector(unittest.TestCase):
  def test_add(self):
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    self.assertEqual(Vector(4, 5), v1+v2)

  def test_mul(self):
    v = Vector(3, 4)
    self.assertEqual(Vector(9, 12), v * 3)

  def test_abs(self):
    v = Vector(3, 4)
    self.assertAlmostEqual(5.0, abs(v))
