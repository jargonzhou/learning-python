"""
Unit test of pythonic object.

support BIF that convert types: repr(), bytes(), complex()
object representation: __repr__, __str__, __bytes__, __format__

alternative constuctor as class method
f-string, format(), str.format()
read-only attribute access
hashable object
private and protected attributes: __xxx, name mangling(in __dict__); _xxx
__slots__: save memory than __dict__
"""
from sys import exception
import unittest

from src.classes_and_protocols.pixel import Pixel, OpenPixel, ColorPixel
from src.classes_and_protocols.vector2d import Vector2d, Vector2dWithoutSlots

# pylint: skip-file


class TestVector2d(unittest.TestCase):
  """tests for Vector2d"""

  def test_vector2d(self) -> None:
    v1 = Vector2d(3, 4)
    # attributes
    self.assertAlmostEqual(3.0, v1.x)
    self.assertAlmostEqual(4.0, v1.y)
    # unpack
    x, y = v1
    self.assertAlmostEqual(3.0, x)
    self.assertAlmostEqual(4.0, y)

    # str
    self.assertEqual('(3.0, 4.0)', str(v1))
    # repr
    self.assertEqual('Vector2d(3.0, 4.0)', repr(v1))

    # eval
    v1_clone = eval(repr(v1))

    # ==: __eq__
    self.assertTrue(v1 == v1_clone)
    # __bytes__
    octets = bytes(v1)
    self.assertEqual(
        b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@', octets)

    # __abs__
    self.assertAlmostEqual(5.0, abs(v1))

    # __bool__
    self.assertTrue(bool(v1))
    self.assertFalse(Vector2d(0, 0))

  def test_override_class_attributes(self) -> None:
    v1 = Vector2dWithoutSlots(1.1, 2.2)
    self.assertEqual(b'd\x9a\x99\x99\x99\x99\x99\xf1?\x9a\x99\x99\x99\x99\x99\x01@',
                     bytes(v1))
    # at instance level
    v1.typecode = 'f'
    self.assertEqual(b'f\xcd\xcc\x8c?\xcd\xcc\x0c@',
                     bytes(v1))
    self.assertEqual('d', Vector2dWithoutSlots.typecode)

    # at class level
    # NOTE: with __slots__: 'Vector2d' object attribute 'typecode' is read-only, see blow
    Vector2dWithoutSlots.typecode = 'f'
    v2 = Vector2dWithoutSlots(1.1, 2.2)
    self.assertEqual(b'f\xcd\xcc\x8c?\xcd\xcc\x0c@',
                     bytes(v2))

    v = Vector2d(1.1, 2.2)
    with self.assertRaises(AttributeError) as cm:
      v.typecode = 'f'
    self.assertEqual("'Vector2d' object attribute 'typecode' is read-only",
                     str(cm.exception))


class TestSlots(unittest.TestCase):
  """tests for __slots__"""

  def test_pixel(self) -> None:
    p = Pixel()

    # have no __dict__
    with self.assertRaises(AttributeError) as cm:
      p.__dict__
    self.assertEqual("'Pixel' object has no attribute '__dict__'",
                     str(cm.exception))
    p.x = 10
    p.y = 20

    # fail to set attributes not in __slots__
    with self.assertRaises(AttributeError) as cm:
      p.color = 'red'
    self.assertEqual("'Pixel' object has no attribute 'color'",
                     str(cm.exception))

  def test_openpixel(self) -> None:
    op = OpenPixel()
    # have __dict__
    self.assertDictEqual({}, op.__dict__)

    # set attribute in __slots__
    # not stored in __dict__, stored in hidden array
    op.x = 8
    self.assertDictEqual({}, op.__dict__)
    self.assertEqual(8, op.x)

    # set attribute not in __slots__: stored in __dict__
    op.color = 'green'
    self.assertDictEqual({'color': 'green'}, op.__dict__)

  def test_color_pixel(self) -> None:
    cp = ColorPixel()
    with self.assertRaises(AttributeError) as cm:
      cp.__dict__
    self.assertEqual("'ColorPixel' object has no attribute '__dict__'",
                     str(cm.exception))
    # attribute in parent class's __slots__
    cp.x = 2
    # attribute in self's __slots__
    cp.color = 'blue'
    # other attribtues
    with self.assertRaises(AttributeError) as cm:
      cp.flavor = 'banana'
    self.assertEqual("'ColorPixel' object has no attribute 'flavor'",
                     str(cm.exception))

  def test_mem(self) -> None:
    # https://github.com/fluentpython/example-code-2e/blob/master/11-pythonic-obj/mem_test.py
    # UNIX
    # import resource

    # NUM_VECTORS = 10000
    # for cls in (Vector2d, Vector2dWithoutSlots):
    #   mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    #   print(f'Creating {NUM_VECTORS:,} {cls.__qualname__!r} instances')
    #   vectors = [cls(3.0, 4.0) for i in range(NUM_VECTORS)]

    #   mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    #   print(f'Initial RAM usage: {mem_init:14,}')
    #   print(f'  Final RAM usage: {mem_final:14,}')
    pass

  def test_mem_windows(self) -> None:
    import tracemalloc

    NUM_VECTORS = 100_0000
    tracemalloc.start()
    for cls in (Vector2dWithoutSlots, Vector2d):
      print(f'Creating {NUM_VECTORS:,} {cls.__qualname__!r} instances')
      vectors = [cls(3.0, 4.0) for i in range(NUM_VECTORS)]
      current, peek = tracemalloc.get_traced_memory()
      print(f'{current / 1024 / 1024:.02f}MB, {peek / 1024 / 1024:.02f}MB')
      tracemalloc.clear_traces()

    # Creating 1,000,000 'Vector2dWithoutSlots' instances
    # 84.35MB, 84.35MB
    # Creating 1,000,000 'Vector2d' instances
    # 53.83MB, 53.83MB
