"""
Example of descriptors.
"""

import abc
from typing import Any, override


class Quantity:
  """descritpor class"""

  def __set_name__(self, owner: Any, name: str) -> None:
    # interpreter calls this on each descriptor it finds in a class body
    # no need __get__()
    self.storage_name = name

  # def __init__(self, storage_name: str) -> None:
  #   self.storage_name = storage_name

  def __init__(self) -> None:
    self.storage_name = None  # type: ignore[assignment]

  def __set__(self, instance: Any, value: Any) -> None:
    if value > 0:
      instance.__dict__[self.storage_name] = value
    else:
      msg = f'{self.storage_name} must be > 0'
      raise ValueError(msg)

  # def __get__(self, instance: Any, owner: Any) -> Any:
  #   # owner: a reference to the managed class
  #   if instance is None:  # accessed through class
  #     return self
  #   return instance.__dict__[self.storage_name]


class LineItem:
  """managed class"""
  weight = Quantity()  # no need to pass 'weight', see __set_name__()
  price = Quantity()

  def __init__(self, description: str, weight: float, price: float):
    self.description = description
    self.weight = weight
    self.price = price

  def subtotal(self) -> float:
    """total"""
    return self.weight * self.price  # type: ignore[operator, no-any-return]

# more descriptors


class Validated(abc.ABC):
  """validation descritpor"""

  def __init__(self) -> None:
    self.storage_name: str = None  # type: ignore[assignment]

  def __set_name__(self, owner: Any, name: str) -> None:
    self.storage_name = name

  def __set__(self, instance: Any, value: Any) -> None:
    value = self.validate(self.storage_name, value)
    instance.__dict__[self.storage_name] = value

  @abc.abstractmethod
  def validate(self, name: str, value: Any) -> Any:
    """return validated value or raise ValueError"""


class Quantity2(Validated):
  """a number > 0"""

  @override
  def validate(self, name: str, value: Any) -> Any:
    if value <= 0:
      raise ValueError(f'{name} must be > 0')
    return value


class NonBlank(Validated):
  """non blank string"""
  @override
  def validate(self, name: str, value: Any) -> Any:
    value = value.strip()
    if not value:
      raise ValueError(f'{name} cannot be blank')
    return value


class LineItem2:
  """managed class"""
  description = NonBlank()
  weight = Quantity()  # no need to pass 'weight', see __set_name__()
  price = Quantity()

  def __init__(self, description: str, weight: float, price: float):
    self.description = description
    self.weight = weight
    self.price = price

  def subtotal(self) -> float:
    """total"""
    return self.weight * self.price  # type: ignore[operator, no-any-return]
