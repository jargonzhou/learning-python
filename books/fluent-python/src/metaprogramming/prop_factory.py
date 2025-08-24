"""
Example of property factory.
"""
from typing import Any


def quantity(storage_name: str) -> property:
  """property factor"""
  def qty_getter(instance: Any) -> Any:
    return instance.__dict__[storage_name]

  def qty_setter(instance: Any, value: Any) -> None:
    if value > 0:
      instance.__dict__[storage_name] = value
    else:
      raise ValueError('value must be > 0')

  return property(qty_getter, qty_setter)


class LineItem:
  """class to use property factory"""
  weight = quantity('weight')
  price = quantity('price')

  def __init__(self, description: str, weight: float, price: float):
    self.description = description
    self.weight = weight  # call setter
    self.price = price

  def subtotal(self) -> float:
    """total"""
    return self.weight * self.price  # type: ignore[no-any-return]
