"""
Example of JSON dynamic attributes.
"""

from __future__ import annotations
from collections.abc import Set, Mapping, MutableSequence
from functools import cache
import inspect
import json
import keyword
from typing import Any


class FrozenJSON:
  """a read-only facade for JSON data using attributes."""

  def __new__(cls, arg: Any) -> Any:
    # flexible object creation
    if isinstance(arg, Mapping):
      return super().__new__(cls)
    if isinstance(arg, MutableSequence):
      return [cls(item) for item in arg]
    return arg

  def __init__(self, mapping: Mapping[str, Any]) -> None:
    self.__data = dict(mapping)
    for k, v in mapping.items():
      if keyword.iskeyword(k):
        k += '_'
      elif not k.isidentifier():
        k = '_' + k
      self.__data[k] = v

  def __getattr__(self, name: str) -> Any:
    # called when no attribute 'name'
    try:
      return getattr(self.__data, name)
    except AttributeError:
      return FrozenJSON.build(self.__data[name])

  def __dir__(self) -> Set[str]:
    # support dir()
    return self.__data.keys()

  @classmethod
  def build(cls, obj: Any) -> Any:
    """class constructor"""
    if isinstance(obj, Mapping):
      return cls(obj)
    if isinstance(obj, MutableSequence):
      return [cls.build(item) for item in obj]
    return obj

# computed properties


def load(path: str = 'tests/metaprogramming/osconfeed.json') -> Mapping[str, Record]:
  """load json data to keyed Records"""
  records = {}
  with open(path, encoding='utf-8') as f:
    raw_data = json.load(f)
  for collection, raw_records in raw_data['Schedule'].items():
    record_type = collection[:-1]  # remvoe 's'
    cls_name = record_type.capitalize()
    # get from module global scope
    cls = globals().get(cls_name, Record)
    if inspect.isclass(cls) and issubclass(cls, Record):
      factory = cls
    else:
      factory = Record
    for raw_record in raw_records:
      key = f'{record_type}.{raw_record["serial"]}'  # example: speaker.341
      records[key] = factory(**raw_record)  # value: Record
  return records


class Record:
  """demonstration of computed properties"""

  # hold data of load()
  __index = None

  def __init__(self, **kwargs: Any) -> None:
    self.__dict__.update(kwargs)

  # autopep8: off
  def __repr__(self) -> str:
    # pylint: disable="no-member"
    return f'<{self.__class__.__name__} serial={self.serial!r}>' # type: ignore[attr-defined]
  # autopep8: on

  @staticmethod
  def fetch(key: str) -> Record:
    """fetch record"""
    if Record.__index is None:
      Record.__index = load()
    return Record.__index[key]  # pylint: disable="unsubscriptable-object"


class Event(Record):
  """event"""

  def __init__(self, **kwargs: Any) -> None:
    self.__speaker_objs: list[Record] = []
    super().__init__(**kwargs)

  def __repr__(self) -> str:
    try:
      # autopep8: off
      return f'<{self.__class__.__name__} {self.name!r}>' # type: ignore[attr-defined]
      # autopep8: on
    except AttributeError:
      return super().__repr__()

  # @cached_property  # cache
  @property
  @cache
  def venue(self) -> Any:
    """venue in event"""
    # pylint: disable="no-member"
    key = f'venue.{self.venue_serial}'  # type: ignore[attr-defined]
    return self.__class__.fetch(key)

  @property
  def speakers(self) -> Any:
    """speakers in event"""
    # cache
    if not hasattr(self, '__speaker_objs'):
      # use __dict__ to avoid recursive call to speakers property
      self.__speaker_objs = [self.__class__.fetch(f'speaker.{speaker_serial}')
                             for speaker_serial in self.__dict__['speakers']]
    return self.__speaker_objs
