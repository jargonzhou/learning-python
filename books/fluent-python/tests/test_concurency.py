"""
Example of testing concurrency code.

test with synchronization
- threading.Lock
- threading.Semaphore
- threading.Event

test asynchronous code
- unittest.IsolatedAsyncioTestCase

??? correctness, liveness verification
"""

# pylint: disable="missing-class-docstring,missing-function-docstring,too-few-public-methods"

import asyncio
import threading
import unittest


################################################################################
# test with synchronization
################################################################################


class SharedResource:
  def __init__(self) -> None:
    self.value = 0
    self.lock = threading.Lock()

  def increment(self) -> None:
    with self.lock:
      self.value += 1


class TestWithSynchronization(unittest.TestCase):
  def test_increment(self) -> None:
    resource = SharedResource()
    threads = []
    for _ in range(10):
      t = threading.Thread(target=resource.increment)
      threads.append(t)
      t.start()

    for t in threads:
      t.join()

    self.assertEqual(10, resource.value)

################################################################################
# test asynchronous code
################################################################################


async def async_f() -> str:
  await asyncio.sleep(.01)
  return "done"


class TestAsync(unittest.IsolatedAsyncioTestCase):
  async def test_async_f(self) -> None:
    result = await async_f()
    self.assertEqual("done", result)
