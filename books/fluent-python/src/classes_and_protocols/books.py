"""
Example of TypedDict
"""

import json
from typing import TypedDict


class BookDict(TypedDict):
  """book dict"""
  isbn: str
  title: str
  authors: list[str]
  pagecount: int


def from_json(data: str) -> BookDict:
  """construct from json"""
  # explicit type annotaion
  book: BookDict = json.loads(data)
  return book
