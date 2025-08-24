"""
Unit test of sequence special methods.

example: a multidimensional Vector class
  final version: P.419
protocols and duck typing
sequence ptotocol: __len__, __getitem__
slicing
dynamic attributes: __getattr__
"""
import array
import unittest
from src.classes_and_protocols.vector import Vector
from typing import Any

# pylint: skip-file
# mypy: disable-error-code="index,attr-defined"


class TestVector(unittest.TestCase):
  def test_vector2d_compatible(self) -> None:
    # __init__, __repr__
    v = Vector([3.1, 4.2])
    self.assertEqual('Vector([3.1, 4.2])', repr(v))
    v = Vector([3, 4, 5])
    self.assertEqual('Vector([3.0, 4.0, 5.0])', repr(v))
    v = Vector(range(10))
    self.assertEqual('Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])', repr(v))

  def test_sliceable_sequence(self) -> None:
    v = Vector([3, 4, 5])
    # len: __len__
    self.assertEqual(3, len(v))
    self.assertTupleEqual((3.0, 5.0), (v[0], v[-1]))

    v = Vector(range(7))
    # slice: __getitem__
    self.assertEqual(array.array('d', [1.0, 2.0, 3.0]), v[1:4])
    self.assertEqual(6.0, v[-1])
    self.assertEqual(Vector([1.0, 2.0, 3.0]), v[1:4])
    self.assertEqual(Vector([6.0]), v[-1:])
    # mypy: disable-error-code="index"
    with self.assertRaises(TypeError) as cm:
      v[1, 2]
    self.assertEqual("'tuple' object cannot be interpreted as an integer",
                     str(cm.exception))

  def test_slice(self) -> None:
    # slice
    class MySeq:
      def __getitem__(self, index: Any) -> Any:
        return index

    s = MySeq()
    self.assertEqual(1, s[1])
    self.assertEqual(slice(1, 4, None), s[1:4])
    self.assertEqual(slice(1, 4, 2), s[1:4:2])
    self.assertEqual((slice(1, 4, 2), 9), s[1:4:2, 9])
    self.assertEqual((slice(1, 4, 2), slice(7, 9, None)), s[1:4:2, 7:9])
    # slice is a class
    self.assertTrue(isinstance(slice(1, 4, None), slice))
    # slice.indices(len)
    self.assertTupleEqual((0, 5, 2), slice(None, 10, 2).indices(5))

  def test_dynamic_attributes(self) -> None:
    # __getattr__
    v = Vector(range(10))
    self.assertEqual(0.0, v.x)
    self.assertTupleEqual((1.0, 2.0, 3.0), (v.y, v.z, v.t))

    # incompatible: without __setattr__
    # v.x = 10
    # self.assertEqual(10, v.x)
    # self.assertEqual(0.0, v[0])

    # __setattr__
    with self.assertRaises(AttributeError) as cm:
      v.x = 10
    self.assertEqual("readonly attribute 'x'",
                     str(cm.exception))

  def test_hashing(self) -> None:
    # __hash__, __eq__
    v = Vector(range(3))
    hash(v)
    with self.assertRaises(TypeError) as cm:
      hash([1])
    self.assertEqual("unhashable type: 'list'", str(cm.exception))
    self.assertEqual(Vector(range(3)), v)

  def test_format(self) -> None:
    # __format__
    self.assertEqual('<2.0, 2.0943951023931957, 2.186276035465284, 3.9269908169872414>',
                     format(Vector([-1, -1, -1, -1]), 'h'))
    self.assertEqual('<4.000e+00, 1.047e+00, 9.553e-01, 7.854e-01>',
                     format(Vector([2, 2, 2, 2]), '.3eh'))
    self.assertEqual('<1.00000, 1.57080, 0.00000, 0.00000>',
                     format(Vector([0, 1, 0, 0]), '0.5fh'))
