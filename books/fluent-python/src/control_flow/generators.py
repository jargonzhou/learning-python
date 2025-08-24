"""
Example of generators
"""


from collections.abc import Generator
from typing import Any


def tree(cls: Any, level: int = 0) -> Generator[Any, Any, Any]:
  """class hierarchy tree generator"""
  yield cls.__name__, level
  for sub_cls in cls.__subclasses__():
    # subgenerators
    yield from tree(sub_cls, level+1)


def display(cls: Any) -> None:
  """display class hierarchy tree"""
  for cls_name, level in tree(cls):
    indent = ' ' * 2 * level
    print(f'{indent}{cls_name}')
