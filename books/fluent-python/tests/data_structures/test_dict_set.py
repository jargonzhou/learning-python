"""
Unit test of dictionary and set.

dict
collections.defaultdict
collections.OrderedDict
collections.ChainMap
collections.Counter
collections.UserDict
collections.abc.Mapping
collections.abc.MutableMapping
shelve.Shelf
types.MappingProxyType

dictionary views: dict_keys, dict_values, dict_items

set
collections.abc.Set
collections.abc.MutableSet
frozenset
"""

# pylint: skip-file

from typing import Any
import unittest
from collections import defaultdict, OrderedDict, ChainMap, Counter, UserDict
from collections.abc import Mapping, MutableMapping, Set, MutableSet
from shelve import Shelf


class TestDict(unittest.TestCase):
  def test_dictcomp(self) -> None:
    dial_codes = [
        (880, 'Bangladesh'),
        (55, 'Brazil'),
        (86, 'China'),
        (91, 'India'),
        (62, 'Indonesia'),
        (81, 'Japan'),
        (234, 'Nigeria'),
        (92, 'Pakistan'),
        (7, 'Russia'),
        (1, 'United States'),
    ]
    country_dial = {country: code for code, country in dial_codes}
    print(country_dial)
    self.assertTrue(isinstance(country_dial, dict))
    # items
    print({code: country.upper()
           for country, code in sorted(country_dial.items())
           if code < 70})

  def test_unpack(self) -> None:
    def dump(**kwargs: Any) -> Any:
      return kwargs
    self.assertDictEqual({'x': 1, 'y': 2, 'z': 3},
                         dump(**{'x': 1}, y=2, **{'z': 3}))
    self.assertDictEqual({'a': 0, 'x': 4, 'y': 2, 'z': 3},
                         {'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}})

  def test_merge(self) -> None:
    d1 = {'a': 1, 'b': 3}
    d2 = {'a': 2, 'b': 4, 'c': 6}
    self.assertDictEqual({'a': 2, 'b': 4, 'c': 6}, d1 | d2)
    d1 |= d2
    self.assertDictEqual({'a': 2, 'b': 4, 'c': 6}, d1)

  def test_pattern_match(self) -> None:

    def get_creators(record: dict) -> list:
      match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
          return names
        case {'type': 'book', 'api': 1, 'author': name}:
          return [name]
        case {'type': 'book'}:
          raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
          return [name]
        case _:
          raise ValueError(f'Invalid record: {record!r}')

    b1 = dict(api=1, author='Douglas Hofstadter',
              type='book', title='Gödel, Escher, Bach')
    self.assertListEqual(['Douglas Hofstadter'],
                         get_creators(b1))

    b2 = OrderedDict(api=2, type='book',
                     title='Python in a Nutshell',
                     authors='Martelli Ravenscroft Holden'.split())
    self.assertListEqual(['Martelli', 'Ravenscroft', 'Holden'],
                         get_creators(b2))

    try:
      get_creators({'type': 'book', 'pages': 770})
    except ValueError as e:
      # Invalid 'book' record: {'type': 'book', 'pages': 770}
      print(e)

    # **extrs
    food = dict(category='ice cream', flavor='vanilla', cost=199)
    match food:
      case {'category': 'ice cream', **details}:
        self.assertDictEqual({'flavor': 'vanilla', 'cost': 199}, details)


class TestMapping(unittest.TestCase):
  def test_abc(self) -> None:
    my_dict: dict[Any, Any] = {}
    self.assertTrue(isinstance(my_dict, Mapping))
    self.assertTrue(isinstance(my_dict, MutableMapping))

  def test_hashable(self) -> None:
    """
    str, bytes
    container types
    forzenset
    tuple
    uder-derined types: id(), __eq__(), __hash__()
    """
    tt = (1, 2, (30, 40))
    hash(tt)
    tl = (1, 2, [30, 40])
    try:
      hash(tl)
    except TypeError as e:
      # unhashable type: 'list'
      print(e)
    tf = (1, 2, frozenset([30, 40]))
    hash(tf)

  def test_insert_update_mutable_values(self) -> None:
    from this import s as Zen
    print(build_word_occurences(Zen))


def build_word_occurences(input: str) -> dict:
  import re
  WORD_RE = re.compile(r'\w+')

  index: dict[str, list[tuple[int, int]]] = {}
  for line_no, line in enumerate(input.splitlines()):
    for match in WORD_RE.finditer(line):
      word = match.group()
      column_no = match.start() + 1
      location = (line_no, column_no)
      # setdefault
      index.setdefault(word, []).append(location)

  return index


class TestDictDive(unittest.TestCase):
  def test_missing_key(self) -> None:
    from this import s as Zen
    # defualtdict
    print(build_word_occurences2(Zen))

    # __missiong__()
    d = StrKeyDict0([('2', 'two'), ('4', 'four')])
    self.assertEqual('two', d['2'])
    try:
      d[1]
    except KeyError as e:
      # '1'
      print(e)


def build_word_occurences2(input: str) -> dict:
  import re
  WORD_RE = re.compile(r'\w+')

  index = defaultdict(list)  # with default_factory
  for line_no, line in enumerate(input.splitlines()):
    for match in WORD_RE.finditer(line):
      word = match.group()
      column_no = match.start() + 1
      location = (line_no, column_no)
      index[word].append(location)

  return index


class StrKeyDict0(dict):
  def __missing__(self, key: Any) -> Any:
    if isinstance(key, str):
      raise KeyError(key)
    return self[str(key)]

  def get(self, key: str, default: Any = None) -> Any:
    try:
      return self[key]
    except KeyError:
      return default

  def __contains__(self, key: Any) -> bool:
    return key in self.keys() or str(key) in self.keys()


class StrKeyDict(UserDict):  # extends UserDict
  def __missing__(self, key: Any) -> Any:
    if isinstance(key, str):
      raise KeyError(key)
    return self[str(key)]

  def __contains__(self, key: Any) -> bool:
    return str(key) in self.data

  def __setitem__(self, key: Any, item: Any) -> None:
    # delegate to self.data
    self.data[str(key)] = item


class TestSet(unittest.TestCase):
  def test_usage(self) -> None:
    l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
    s = set(l)
    self.assertTrue(isinstance(s, set))
    self.assertEqual(type(s), set)
    self.assertSetEqual({'eggs', 'spam', 'bacon'}, s)

  def test_setcomp(self) -> None:
    s = {i for i in range(3)}
    self.assertSetEqual({0, 1, 2}, s)

  def test_operation(self) -> None:
    """
    Mathematical set operations: & intersection() | union() - difference() ^ symmetric_difference()
    Set comparison: in <= issubset() < >= issuperset() > isdisjoint()
    """
    pass
