"""
Example of variance: 
- invariant
- covariant
- contravariant
"""

# pylint: disable="too-few-public-methods,missing-class-docstring,missing-function-docstring,unused-argument"

################################################################################
# invariant
################################################################################


from typing import TypeVar, Generic


class Beverage:
  """饮料"""


class Juice(Beverage):
  """果汁"""


class OrangeJuice(Juice):
  """橙汁"""


T = TypeVar('T')


class BeverageDispenser(Generic[T]):
  """饮料自动售卖机"""

  def __init__(self, beverage: T) -> None:
    self.beverage = beverage

  def dispense(self) -> T:
    return self.beverage


def install(dispenser: BeverageDispenser[Juice]) -> None:
  """install a juice dispenser"""

################################################################################
# covariant
################################################################################


T_co = TypeVar('T_co', covariant=True)


class BeverageDispenserCo(Generic[T_co]):
  """饮料自动售卖机"""

  def __init__(self, beverage: T_co) -> None:
    self.beverage = beverage

  def dispense(self) -> T_co:
    return self.beverage


def install_co(dispenser: BeverageDispenserCo[Juice]) -> None:
  """install a juice dispenser"""

################################################################################
# contravariant
################################################################################


class Refuse:
  """垃圾"""


class Biodegradable(Refuse):
  """可生物降解的垃圾"""


class Compostable(Biodegradable):
  """合成物垃圾"""


T_contra = TypeVar('T_contra', contravariant=True)


class TrashCan(Generic[T_contra]):
  def put(self, refuse: T_contra) -> None:
    """store trash"""


def deploy(trash_can: TrashCan[Biodegradable]) -> None:
  """deploy a trash can for biodegradable refuse"""
