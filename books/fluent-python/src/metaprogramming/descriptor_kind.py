"""
Example of overriding and non-overriding descriptors.
"""

# auxiliary functions

from typing import Any


def cls_name(obj_or_cls: Any) -> str:
  """return class name"""
  cls = type(obj_or_cls)
  if cls is type:
    cls = obj_or_cls
  return cls.__name__.split('.')[-1]


def display(obj: Any) -> str:
  """return display string"""
  cls = type(obj)
  if cls is type:
    return f'<class {obj.__name__}>'
  if cls in [type(None), int]:
    return repr(obj)
  return f'<{cls_name(obj)} object>'


def print_args(name: str, *args: Any) -> None:
  """print args"""
  pseudo_args = ', '.join(display(x) for x in args)
  print(f'-> {cls_name(args[0])}.__{name}__({pseudo_args})')


class Overrding:
  """data descriptor or enforced descriptor"""

  def __get__(self, instance: Any, owner: Any) -> Any:
    print_args('get', self, instance, owner)
    return None

  def __set__(self, instance: Any, value: Any) -> None:
    print_args('set', self, instance, value)


class OverridingNoGet:
  """overriding descriptor without ``__get__``"""

  def __set__(self, instance: Any, value: Any) -> None:
    print_args('set', self, instance, value)


class NonOverrding:
  """non-data or shadowable descriptor: without ``__set__``"""

  def __get__(self, instance: Any, owner: Any) -> Any:
    print_args('get', self, instance, owner)
    return None


class Managed:
  """managed class"""
  over = Overrding()
  over_no_get = OverridingNoGet()
  non_over = NonOverrding()

  def spam(self) -> None:
    """spam"""
    print(f'-> Managed.spam({display(self)})')
