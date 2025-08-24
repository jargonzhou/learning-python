"""
saving memory with __slots__
"""

# pylint: disable=too-few-public-methods


class Pixel:
  """pixel"""
  # stored in a hidden array or references
  # use less memory than __dict__
  __slots__ = ('x', 'y')  # tuple or list


class OpenPixel(Pixel):
  """open pixel"""


class ColorPixel(Pixel):
  """color pixel"""
  # make sure no __dict__
  __slots__ = ('color',)
