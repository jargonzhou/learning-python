"""
Example of use property for attribute validation.
"""


class LineItem:
  """line item in order"""

  def __init__(self, description: str, weight: float, price: float):
    self.description = description
    self.weight = weight  # call setter
    self.price = price

  def subtotal(self) -> float:
    """total"""
    return self.weight * self.price

  @property
  def weight(self) -> float:
    """weight"""
    return self.__weight

  @weight.setter
  def weight(self, value: float) -> None:
    # do validation
    if value > 0:
      self.__weight = value
    else:
      raise ValueError('value must be > 0')


class LineItem2:
  """line item in order: use property class"""

  def __init__(self, description: str, weight: float, price: float):
    self.description = description
    self.__weight: float = -1.0
    self.weight = weight  # call setter
    self.price = price

  def subtotal(self) -> float:
    """total"""
    return self.weight * self.price  # type: ignore[no-any-return]

  def get_weight(self) -> float:
    """weight"""
    return self.__weight

  def set_weight(self, value: float) -> None:
    """set weight"""
    # do validation
    if value > 0:
      self.__weight = value
    else:
      raise ValueError('value must be > 0')

  weight = property(get_weight, set_weight)
