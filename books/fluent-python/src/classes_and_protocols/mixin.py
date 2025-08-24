"""
Example of mixing classes
"""

# pylint: disable="abstract-method"
# mypy: disable-error-code="misc, no-any-return"

import collections
from typing import Any


def _upper(key: Any) -> Any:
  try:
    return key.upper()
  except AttributeError:
    return key


class UpperCaseMixin:
  """case-insentive string key access, uppercase keys when added or looked up

  super()
  """

  def __setitem__(self, key: Any, item: Any) -> None:
    super().__setitem__(_upper(key), item)

  def __getitem__(self, key: Any) -> Any:
    return super().__getitem__(_upper(key))

  def get(self, key: Any, default: Any = None) -> Any:
    """get"""
    return super().get(_upper(key), default)

  def __contains__(self, key: Any) -> bool:
    return super().__contains__(_upper(key))


class UpperDict(UpperCaseMixin, collections.UserDict):
  """uppercase dict"""


class UpperCounter(UpperCaseMixin, collections.Counter):
  """upercase string keys counter"""
