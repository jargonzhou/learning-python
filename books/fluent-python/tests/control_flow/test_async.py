"""
Unit test of asynchronous programming.

async def, await

async with
- __aenter__
- __aexit__

asyncio
- sleep()
- run()
- gather()
- as_completed()
- Semaphore
- to_thread(): replace get_running_loop(), run_in_executor()
- Server: TCP server
  - asyncio.start_server()
  - serve_forever()
- StreamReader, StreamWriter
  
async for
- __aiter__
- __anext__
- `async def` + `yield`: async generator functions
  - `collections.abc.AsyncIterator`
- `async for` + `await`: async comprehension, async generator expression
  
async REPL: `python -m asyncio`

@asynccontextmanager: contextlib

Curio

type hinting
- `typing`: Coroutine, AsyncContextManager, AsyncIterable, AsyncIterator, AsyncGenerator, Awaitable
"""
# pylint: skip-file

import unittest
