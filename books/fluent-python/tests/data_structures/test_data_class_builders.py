"""
Unit test of data class builders.

collections.namedtuple
typing.NamedTuple
@dataclasses.dataclass


type hint
Mypy: a linter
"""
# pylint: skip-file

from collections import namedtuple
import typing
from dataclasses import dataclass
import unittest


class Coordinate:
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon


class Coordinate2(typing.NamedTuple):
  lat: float
  lon: float

  def __str__(self):
    ns = 'N' if self.lat >= 0 else 'S'
    we = 'E' if self.lon >= 0 else 'W'
    return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


@dataclass
class Coordinate3:
  lat: float
  lon: float

  def __str__(self):
    ns = 'N' if self.lat >= 0 else 'S'
    we = 'E' if self.lon >= 0 else 'W'
    return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


class TestDataClassBuilder(unittest.TestCase):
  def test_namedtuple(self):
    Coordinate = namedtuple('Coordinate', 'lat lon')
    self.assertTrue(issubclass(Coordinate, tuple))
    c = Coordinate(55.756, 37.617)
    self.assertEqual(c, Coordinate(55.756, 37.617))

  def test_NamedTuple(self):
    Coordinate = typing.NamedTuple(
        'Coordinate', [('lat', float), ('lon', float)])
    self.assertTrue(Coordinate, tuple)
    # {'lat': <class 'float'>, 'lon': <class 'float'>}
    print(typing.get_type_hints(Coordinate))

    # TypeError: issubclass() arg 2 must be a class, a tuple of classes, or a union
    # self.assertFalse(issubclass(Coordinate2, typing.NamedTuple))
    self.assertTrue(issubclass(Coordinate2, tuple))

  def test_dataclass(self):
    self.assertFalse(issubclass(Coordinate3, tuple))
    self.assertTrue(issubclass(Coordinate3, object))
