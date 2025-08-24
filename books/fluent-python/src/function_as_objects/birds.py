# pylint: skip-file

from typing import Any


class Bird:
  pass


class Duck(Bird):
  def quack(self) -> None:
    print('Quack!')


def alert(birdie: Any) -> None:
  birdie.quack()


def alert_duck(birdie: Duck) -> None:
  birdie.quack()


def alert_bird(birdie: Bird) -> None:
  # "Bird" has no attribute "quack"
  birdie.quack()
