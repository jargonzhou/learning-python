"""
Example of multiple inheritance and MRO(method resolution order).
"""

# pylint: disable="missing-class-docstring,missing-function-docstring,too-few-public-methods,no-member"
# mypy: disable-error-code="misc"

from typing import Any, override


class Root:
  def ping(self) -> None:
    print(f'{self}.ping() in Root')

  def pong(self) -> None:
    print(f'{self}.pong() in Root')

  def __repr__(self) -> str:
    cls_name = type(self).__name__
    return f'<instance of {cls_name}>'


class A(Root):
  @override
  def ping(self) -> None:
    print(f'{self}.ping() in A')
    super().ping()

  @override
  def pong(self) -> None:
    print(f'{self}.pong() in A')
    super().pong()


class B(Root):
  @override
  def ping(self) -> None:
    print(f'{self}.ping() in B')
    super().ping()

  @override
  def pong(self) -> None:
    print(f'{self}.pong() in B')


class Leaf(A, B):
  @override
  def ping(self) -> None:
    print(f'{self}.ping() in Leaf')
    super().ping()


class U():
  def ping(self) -> None:
    print(f'{self}.ping() in U')
    super().ping()  # ???


class LeafUA(U, A):
  @override
  def ping(self) -> None:
    print(f'{self}.ping() in LeafUA')
    super().ping()


def print_mro(cls: Any) -> None:
  """output mro of classes"""
  print(', '.join(c.__name__ for c in cls.__mro__))
