"""
Design patterns with functions.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal
from collections.abc import Sequence
from typing import Callable, NamedTuple, Optional, override

# pylint: disable=too-few-public-methods


################################################################################
# classic strategy pattern
################################################################################
class Customer(NamedTuple):
  """customer"""
  name: str
  fidelity: int


class LineItem(NamedTuple):
  """order item"""
  product: str
  quantity: int
  price: Decimal

  def total(self) -> Decimal:
    """total price"""
    return self.price * self.quantity


class Order(NamedTuple):
  """then context in strategy pattern"""
  customer: Customer
  cart: Sequence[LineItem]
  promotion: Optional['Promotion'] = None

  def total(self) -> Decimal:
    """total price"""
    totals = (item.total() for item in self.cart)
    return sum(totals, start=Decimal(0))

  def due(self) -> Decimal:
    """final total price"""
    if self.promotion is None:
      discount = Decimal(0)
    else:
      discount = self.promotion.discount(self)
    return self.total() - discount

  def __repr__(self) -> str:
    """repr"""
    return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'


class Promotion(ABC):
  """promotion"""
  @abstractmethod
  def discount(self, order: Order) -> Decimal:
    """return discount as a positive dollar amount"""


class FidelityPromo(Promotion):  # first Concrete Strategy
  """5% discount for customers with 1000 or more fidelity points"""

  def discount(self, order: Order) -> Decimal:
    rate = Decimal('0.05')
    if order.customer.fidelity >= 1000:
      return order.total() * rate
    return Decimal(0)


class BulkItemPromo(Promotion):  # second Concrete Strategy
  """10% discount for each LineItem with 20 or more units"""

  def discount(self, order: Order) -> Decimal:
    discount = Decimal(0)
    for item in order.cart:
      if item.quantity >= 20:
        discount += item.total() * Decimal('0.1')
    return discount


class LargeOrderPromo(Promotion):  # third Concrete Strategy
  """7% discount for orders with 10 or more distinct items"""

  def discount(self, order: Order) -> Decimal:
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
      return order.total() * Decimal('0.07')
    return Decimal(0)

################################################################################
# function-oriented strategy pattern
################################################################################


@dataclass(frozen=True)
class Order2:
  """the content"""
  customer: Customer
  cart: Sequence[LineItem]
  promotion: Optional[Callable[['Order2'], Decimal]] = None

  def total(self) -> Decimal:
    """total price"""
    totals = (item.total() for item in self.cart)
    return sum(totals, start=Decimal(0))

  def due(self) -> Decimal:
    """final total price"""
    if self.promotion is None:
      discount = Decimal(0)
    else:
      discount = self.promotion(self)
    return self.total() - discount

  def __repr__(self) -> str:
    """repr"""
    return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'


def fidelity_promo(order: Order2) -> Decimal:
  """5% discount for customers with 1000 or more fidelity points"""
  if order.customer.fidelity >= 1000:
    return order.total() * Decimal('0.05')
  return Decimal(0)


def bulk_item_promo(order: Order2) -> Decimal:
  """10% discount for each LineItem with 20 or more units"""
  discount = Decimal(0)
  for item in order.cart:
    if item.quantity >= 20:
      discount += item.total() * Decimal('0.1')
  return discount


def large_order_promo(order: Order2) -> Decimal:
  """7% discount for orders with 10 or more distinct items"""
  distinct_items = {item.product for item in order.cart}
  if len(distinct_items) >= 10:
    return order.total() * Decimal('0.07')
  return Decimal(0)


################################################################################
# command pattern
################################################################################
class Command(ABC):
  """command"""
  @abstractmethod
  def execute(self) -> None:
    """execute command"""


class OpenCommand(Command):
  """open command"""
  @override
  def execute(self) -> None:
    print('open ...')


class PasteCommand(Command):
  """paste command"""
  @override
  def execute(self) -> None:
    print('paste ...')


class MacroCommand(Command):
  """macro commands"""

  def __init__(self, commands: list[Command]):  # composition
    self.commands = commands

  @override
  def execute(self) -> None:
    print('macro ...')
    for command in self.commands:
      command.execute()

  def __call__(self) -> None:
    self.execute()
