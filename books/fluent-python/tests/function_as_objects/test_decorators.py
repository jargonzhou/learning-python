"""
Unit test of decorators and closures.
"""
import time
from typing import Any
import unittest
from src.function_as_objects.decorators import Averager, make_averager, make_averager2, \
    register, registry, register_f, target, \
    clock, clock2, clock_c, clock_p

# pylint: skip-file
# mypy: disable-error-code="used-before-def,has-type"

bb: int = 3


class TestDecorators(unittest.TestCase):
  def test_decorator_101(self) -> None:
    # running inner()
    target()
    # <function deco.<locals>.inner at 0x000001E172BC56C0>
    print(target)

  def test_decorators_run_at_import_time(self) -> None:
    @register
    def f1() -> None:
      """f1"""
      print('running f1()')

    @register
    def f2() -> None:
      """f2"""
      print('running f2()')

    def f3() -> None:
      """f3"""
      print('running f3()')
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

    # running register(f1)
    # running register(f2)
    # running main()
    # registry -> [<function TestDecorators.test_decorators_run_at_import_time.<locals>.f1 at 0x0000021D6E49C900>, <function TestDecorators.test_decorators_run_at_import_time.<locals>.f2 at 0x0000021D6E49C860>]
    # running f1()
    # running f2()
    # running f3()

  def test_variable_scope_rules(self) -> None:
    def f1(a: Any) -> None:
      print(a)
      print(b)  # "b" is not defined
    try:
      f1(3)
    except NameError as e:
      # cannot access free variable 'b' where it is not associated with a value in enclosing scope
      print(e)

    b = 6
    f1(3)

    def f2(a: Any) -> None:
      print(a)
      # mypy: disable-error-code="used-before-def,has-type"
      print(b)  # Name "b" is used before definition
      b = 9
    try:
      f2(3)
    except UnboundLocalError as e:
      # cannot access local variable 'b' where it is not associated with a value
      print(e)

    def f3(a: Any) -> None:
      global bb  # global variable
      print(a)
      print(bb)
      bb = 9
    f3(3)
    self.assertEqual(9, bb)

  def test_clock(self) -> None:
    @clock
    def snooze(seconds: float) -> None:
      import time
      time.sleep(seconds)

    snooze(0.1)

    @clock
    def factorial(n: int) -> int:
      return 1 if n < 2 else n*factorial(n-1)

    factorial(6)
    self.assertEqual('clocked', factorial.__name__)

    @clock2
    def factorial2(n: int) -> int:
      return 1 if n < 2 else n*factorial(n-1)
    factorial2(n=6)
    self.assertEqual('factorial2', factorial2.__name__)

  def test_parameterized_decorator(self) -> None:
    @register_f(active=False)
    def f1() -> None:
      print('running f1()')

    @register_f()
    def f2() -> None:
      print('running f2()')

    def f3() -> None:
      print('running f3()')

    # running register factory (active=False->decorate<function TestDecorators.test_parameterized_decorator.<locals>.f1 at 0x000001EE215D8360>
    # running register factory (active=True->decorate<function TestDecorators.test_parameterized_decorator.<locals>.f2 at 0x000001EE215DA7A0>

  def test_parameterized_clock(self) -> None:
    @clock_p('{name}: {elapsed}s')
    def snooze(seconds: float) -> None:
      time.sleep(seconds)
    for i in range(3):
      snooze(.123)

    # snooze: 0.1232769999987795s
    # snooze: 0.12337150000530528s
    # snooze: 0.12343569999939064s

  def test_class_based_click(self) -> None:
    @clock_c('{name}: {elapsed}s')
    def snooze(seconds: float) -> None:
      time.sleep(seconds)
    for i in range(3):
      snooze(.123)

    # snooze: 0.12345140000252286s
    # snooze: 0.12338230000023032s
    # snooze: 0.12346670000260929s


class TestClosure(unittest.TestCase):
  def test_avg_class(self) -> None:
    avg = Averager()
    self.assertAlmostEqual(10.0, avg(10.0))
    self.assertAlmostEqual(10.5, avg(11.0))
    self.assertAlmostEqual(11.0, avg(12.0))

  def test_avg_with_clousure(self) -> None:
    avg = make_averager()
    self.assertAlmostEqual(10.0, avg(10.0))
    self.assertAlmostEqual(10.5, avg(11.0))
    self.assertAlmostEqual(11.0, avg(12.0))

    # inspect function created
    # local variables
    self.assertTupleEqual(('new_value', 'total'), avg.__code__.co_varnames)
    # free variables
    self.assertTupleEqual(('series',), avg.__code__.co_freevars)
    # closure cells: for free variables
    if avg.__closure__ is not None:
      self.assertListEqual([10, 11, 12], avg.__closure__[0].cell_contents)

  def test_nonlocal(self) -> None:
    avg = make_averager2()
    self.assertAlmostEqual(10.0, avg(10.0))
    self.assertAlmostEqual(10.5, avg(11.0))
    self.assertAlmostEqual(11.0, avg(12.0))
