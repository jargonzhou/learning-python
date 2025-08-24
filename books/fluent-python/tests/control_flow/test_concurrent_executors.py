"""
Unit test of concurrent executors.

`concurrent.futures.Executor`
- ThreadPoolExecutor
- ProcessPoolExecutor
- methods:
  - submit()
  - map()

futures
- `concurrent.futures.Future`
- `asyncio.Future`
- methods: 
  - done(), add_done_callback(), result()
  - concurrent.futures.as_completed()
  - asyncio.as_completed()

"""
# pylint: skip-file


import unittest
