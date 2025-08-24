"""
Unit test of design patterns with functions.

Strategy
- Order
- Promotion
  - FidelityPromo
  - BulkItemPromo
  - LargeOrderPromo

Command
- OpenCommand
- PasteCommand
- MacroCommand
"""
from decimal import Decimal
from typing import Callable
import unittest

from src.function_as_objects.function_design_patterns import Customer, LineItem, MacroCommand, OpenCommand, \
    Order, FidelityPromo, BulkItemPromo, LargeOrderPromo, \
    Order2, PasteCommand, fidelity_promo, bulk_item_promo, large_order_promo

# pylint: skip-file

joe = Customer('John Doe', 0)
ann = Customer('Ann SMith', 1100)
cart = (LineItem('banana', 4, Decimal('.5')),
        LineItem('apple', 10, Decimal('1.5')),
        LineItem('watermelon', 5, Decimal(5)))
banana_cart = (LineItem('banana', 30, Decimal('.5')),
               LineItem('apple', 10, Decimal('1.5')))
long_cart = tuple(LineItem(str(sku), 1, Decimal(1)) for sku in range(10))

# put here: type!!!
# put in method: variable
Promotion2 = Callable[[Order2], Decimal]


class TestStrategyPattern(unittest.TestCase):
  def test_classic_strategy(self) -> None:
    order = Order(joe, cart, FidelityPromo())
    self.assertAlmostEqual(Decimal(42.00), order.total())
    self.assertAlmostEqual(Decimal(42.00), order.due())
    order = Order(ann, cart, FidelityPromo())
    self.assertAlmostEqual(Decimal(42.00), order.total())
    self.assertAlmostEqual(Decimal(39.90), order.due())

    order = Order(joe, banana_cart, BulkItemPromo())
    self.assertAlmostEqual(Decimal(30.00), order.total())
    self.assertAlmostEqual(Decimal(28.50), order.due())

    order = Order(joe, long_cart, LargeOrderPromo())
    self.assertAlmostEqual(Decimal(10.00), order.total())
    self.assertAlmostEqual(Decimal(9.30), order.due())

    order = Order(joe, cart, LargeOrderPromo())
    self.assertAlmostEqual(Decimal(42.00), order.total())
    self.assertAlmostEqual(Decimal(42.00), order.due())

  def test_function_oriented_strategy(self) -> None:
    order = Order2(joe, cart, fidelity_promo)
    self.assertAlmostEqual(Decimal(42.00), order.total())
    self.assertAlmostEqual(Decimal(42.00), order.due())
    order = Order2(ann, cart, fidelity_promo)
    self.assertAlmostEqual(Decimal(42.00), order.total())
    self.assertAlmostEqual(Decimal(39.90), order.due())

    order = Order2(joe, banana_cart, bulk_item_promo)
    self.assertAlmostEqual(Decimal(30.00), order.total())
    self.assertAlmostEqual(Decimal(28.50), order.due())

    order = Order2(joe, long_cart, large_order_promo)
    self.assertAlmostEqual(Decimal(10.00), order.total())
    self.assertAlmostEqual(Decimal(9.30), order.due())

    order = Order2(joe, cart, large_order_promo)
    self.assertAlmostEqual(Decimal(42.00), order.total())
    self.assertAlmostEqual(Decimal(42.00), order.due())

    # best promotion
    promos = [fidelity_promo, bulk_item_promo, large_order_promo]

    def best_promo(order: Order2) -> Decimal:
      """Compute the best discount available"""
      return max(promo(order) for promo in promos)

    order = Order2(joe, long_cart, best_promo)
    self.assertAlmostEqual(Decimal(10.00), order.total())
    self.assertAlmostEqual(Decimal(9.30), order.due())
    order = Order2(joe, banana_cart, best_promo)
    self.assertAlmostEqual(Decimal(30.00), order.total())
    self.assertAlmostEqual(Decimal(28.50), order.due())
    order = Order2(ann, cart, best_promo)
    self.assertAlmostEqual(Decimal(42.00), order.total())
    self.assertAlmostEqual(Decimal(39.90), order.due())

  def test_find_strategy_in_module(self) -> None:
    # globals(): current global symbol table
    _promos: list[Callable[['Order2'], Decimal]] = [promo for name, promo in globals().items()
                                                    if name.endswith('_promo') and
                                                    name != 'best_promo']

    def _best_promo(order: Order2) -> Decimal:
      """Compute the best discount available"""
      return max((promo(order) for promo in _promos))

    order = Order2(joe, long_cart, _best_promo)
    self.assertAlmostEqual(Decimal(10.00), order.total())
    self.assertAlmostEqual(Decimal(9.30), order.due())
    order = Order2(joe, banana_cart, _best_promo)
    self.assertAlmostEqual(Decimal(30.00), order.total())
    self.assertAlmostEqual(Decimal(28.50), order.due())
    order = Order2(ann, cart, _best_promo)
    self.assertAlmostEqual(Decimal(42.00), order.total())
    self.assertAlmostEqual(Decimal(39.90), order.due())

  def test_find_strategy_in_module_introspect(self) -> None:
    # inspect
    import inspect
    import src.function_as_objects.function_design_patterns as m
    _promos: list[Callable[['Order2'], Decimal]] = [
        func for name, func in inspect.getmembers(m, inspect.isfunction)
        if name not in {'NamedTuple', 'abstractmethod', 'dataclass'}]
    print(_promos)

    def _best_promo(order: Order2) -> Decimal:
      """Compute the best discount available"""
      return max((promo(order) for promo in _promos))

    order = Order2(joe, long_cart, _best_promo)
    self.assertAlmostEqual(Decimal(10.00), order.total())
    self.assertAlmostEqual(Decimal(9.30), order.due())
    order = Order2(joe, banana_cart, _best_promo)
    self.assertAlmostEqual(Decimal(30.00), order.total())
    self.assertAlmostEqual(Decimal(28.50), order.due())
    order = Order2(ann, cart, _best_promo)
    self.assertAlmostEqual(Decimal(42.00), order.total())
    self.assertAlmostEqual(Decimal(39.90), order.due())

  def test_decorator_enhanced_strategy(self) -> None:
    promos: list[Promotion2] = []

    def promotion(promo: Promotion2) -> Promotion2:
      """the decorator"""
      promos.append(promo)
      return promo

    def _best_promo(order: Order2) -> Decimal:
      """Compute the best discount available"""
      return max(promo(order) for promo in promos)

    @promotion
    def fidelity(order: Order2) -> Decimal:
      """5% discount for customers with 1000 or more fidelity points"""
      if order.customer.fidelity >= 1000:
        return order.total() * Decimal('0.05')
      return Decimal(0)

    @promotion
    def bulk_item(order: Order2) -> Decimal:
      """10% discount for each LineItem with 20 or more units"""
      discount = Decimal(0)
      for item in order.cart:
        if item.quantity >= 20:
          discount += item.total() * Decimal('0.1')
      return discount

    @promotion
    def large_order(order: Order2) -> Decimal:
      """7% discount for orders with 10 or more distinct items"""
      distinct_items = {item.product for item in order.cart}
      if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
      return Decimal(0)

    order = Order2(joe, long_cart, _best_promo)
    self.assertAlmostEqual(Decimal(10.00), order.total())
    self.assertAlmostEqual(Decimal(9.30), order.due())
    order = Order2(joe, banana_cart, _best_promo)
    self.assertAlmostEqual(Decimal(30.00), order.total())
    self.assertAlmostEqual(Decimal(28.50), order.due())
    order = Order2(ann, cart, _best_promo)
    self.assertAlmostEqual(Decimal(42.00), order.total())
    self.assertAlmostEqual(Decimal(39.90), order.due())


class TestCommandPatter(unittest.TestCase):
  def test_command(self) -> None:
    open_command = OpenCommand()
    paste_command = PasteCommand()
    macro_command = MacroCommand([open_command, paste_command])
    macro_command()

    # macro ...
    # open ...
    # paste ...
