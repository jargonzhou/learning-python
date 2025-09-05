
# Python Tools

## Skafold
* [cookiecutter](./cookiecutter/cookiecutter.md)
* [PyScaffold](./PyScaffold.md)

## Environment
* [click](https://github.com/pallets/click): Python composable command line interface toolkit.
* [IPython](./ipython/IPython.md)
* [Miniconda](https://docs.anaconda.com/miniconda/):  Miniconda is a free, miniature installation of Anaconda Distribution that includes only conda, Python, the packages they both depend on, and a small number of other useful packages.
* [Pipenv.md](./Pipenv.md): Pipenv is a Python virtualenv management tool that supports a multitude of systems and nicely bridges the gaps between `pip`, `python` (using system python, `pyenv` or `asdf`) and `virtualenv`.
* [pyenv](https://github.com/pyenv/pyenv): pyenv lets you easily **switch between multiple versions of Python**. It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.
* [Python Tutor](https://pythontutor.com/): Online Compiler, Visual Debugger, and AI Tutor for Python, Java, C, C++, and JavaScript
* [python-dotenv](https://github.com/theskumar/python-dotenv): Reads key-value pairs from a .env file and can set them as environment variables. It helps in developing applications following the 12-factor principles.
* [virtualenv](./virtualenv.md): a tool to create isolated Python environments. Since Python 3.3, a subset of it has been integrated into the standard library under the `venv` module.

## Package, Project
* [pip.md](./pip.md): pip is the package installer for Python.
* [pipx](https://pipx.pypa.io/): Install and Run Python Applications in Isolated Environments
* [Poetry](./poetry/Poetry.md): Python packaging and dependency management made easy.
* [pydoc](../language/std/pydoc.md)
* [Setuptools](https://setuptools.pypa.io/en/latest/userguide/index.html): Setuptools is a fully-featured, actively-maintained, and stable library designed to facilitate packaging Python projects. It helps developers to easily share reusable code (in the form of a library) and programs (e.g., CLI/GUI tools implemented in Python), that can be installed with pip and uploaded to PyPI.
* [tox](./tox.md): tox aims to automate and standardize testing in Python.
* [uv](./uv.md): An extremely fast Python package and project manager, written in Rust.

## Documentation
* [Jupyter Book](https://github.com/jupyter-book/jupyter-book): Jupyter Book is an open-source tool for building publication-quality books and documents from computational material.
* [MkDocs](https://github.com/mkdocs/mkdocs): MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file. It is designed to be easy to use and can be extended with third-party themes, plugins, and Markdown extensions.
* [Read the Docs](https://about.readthedocs.com/): Docs as Code for everyone. Empower your team with versioned documentation, seamless previews, and powerful authentication. All integrated into your Git workflow.
* [Sphinx](https://github.com/sphinx-doc/sphinx): The Sphinx documentation generator. Sphinx uses reStructuredText as its markup language, and many of its strengths come from the power and straightforwardness of reStructuredText and its parsing and translating suite, the Docutils.

## Template
* [Jinja](./Jinja.md): Jinja is a fast, expressive, extensible templating engine

## Linter, Formatter, Type Checker
* [autopep8](./autopep8.md): autopep8 automatically formats Python code to conform to the PEP 8 style guide.
* [Black](./Black.md): The uncompromising code formatter.
* [blue](https://pypi.org/project/blue/): Blue -- Some folks like black but I prefer blue.
* [flake8](http://flake8.pycqa.org/en/latest/index.html): flake8 is a python tool that glues together pycodestyle, pyflakes, mccabe, and third-party plugins to check the style and quality of some python code.
* [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
* [Mypy](./mypy.md): Static Typing for Python.
* [pycodestyle.md](./pycodestyle.md)
* [Pylint](./pylint/pylint.md): a static code analyser for Python 2 or 3.
* [Pyre](https://github.com/facebook/pyre-check): Performant type-checking for python. - Facebook
* [Pyright](https://github.com/microsoft/pyright): Static Type Checker for Python. - Microsoft
* [Pytype](https://github.com/google/pytype): A static type analyzer for Python code. - Google
* [typeshed](https://github.com/python/typeshed): Collection of library stubs for Python, with static types. - `pyi` stub files

## Testing
* [Coverage.py](https://github.com/nedbat/coveragepy): Code coverage measurement for Python.
* [Faker](./Faker.md): Faker is a Python package that generates fake data for you.
* [Hypothesis](https://github.com/HypothesisWorks/hypothesis): The property-based testing library for Python.
* [Locust](https://locust.io/): Locust is an open source performance/load testing tool for HTTP and other protocols. Its developer-friendly approach lets you define your tests in regular Python code.
* [mock](https://mock.readthedocs.io/en/latest/): mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used. mock is now part of the Python standard library, available as `unittest.mock` in Python 3.3 onwards.
* [Playwright](https://github.com/microsoft/playwright): Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API.
* [pytest](./pytest.md): The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.
* [Selenium](https://github.com/SeleniumHQ/selenium): A browser automation framework and ecosystem.
* [shuffler](https://github.com/qweeze/shuffler): A concurrency testing tool for python. Aims to help finding concurrency issues by exploring various possible interleavings of atomic operations within multiple concurrent threads/coroutines.

## Logging
* [logging](https://docs.python.org/3/library/logging.html): Logging facility for Python.
  * [LogRecord attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes)
* [python-json-logger](https://github.com/nhairs/python-json-logger): Python JSON Logger enables you produce JSON logs when using Python's `logging` package.

## Concurrency, Parallel
* [Curio](https://github.com/dabeaz/curio): Curio is a coroutine-based library for concurrent Python systems programming using `async`/`await`. It provides standard programming abstractions such as tasks, sockets, files, locks, and queues as well as some advanced features such as support for structured concurrency. It works on Unix and Windows and has zero dependencies. You'll find it to be familiar, small, fast, and fun.
* [Dask](https://github.com/dask/dask): Dask is a flexible parallel computing library for analytics.
* [greenlet](https://github.com/python-greenlet/greenlet/): greenlets are lightweight coroutines for in-process sequential concurrent programming.
* [Pykka](https://github.com/jodal/pykka): Pykka is a Python implementation of the actor model. The actor model introduces some simple rules to control the sharing of state and cooperation between execution units, which makes it easier to build concurrent applications.
* [Thespian](https://github.com/thespianpy/Thespian): Python Actor concurrency library.
* [Trio](https://github.com/python-trio/trio): a friendly Python library for async concurrency and I/O.

## Database
* [aiomysql](https://github.com/aio-libs/aiomysql): aiomysql is a library for accessing a MySQL database from the asyncio.
* [asyncmy](https://github.com/long2ice/asyncmy): A fast asyncio MySQL/MariaDB driver with replication protocol support.
* [asyncpg](https://github.com/MagicStack/asyncpg): A fast PostgreSQL Database Client Library for Python/asyncio.
* [JupySQL](./JupySQL.ipynb): Run SQL in Jupyter/IPython via a `%sql` and `%%sql` magics.
* [Motor](https://github.com/mongodb/motor): the async Python driver for MongoDB and Tornado or asyncio. As of May 14th, 2025, Motor is deprecated in favor of the GA release of the *PyMongo* Async API.
* [Pydantic](https://docs.pydantic.dev/): Pydantic is the most widely used data validation library for Python.
* [PyMongo](https://github.com/mongodb/mongo-python-driver): the Official MongoDB Python driver.
* [PyMySQL](./PyMySQL.ipynb)
* [SQLAlchemy](./SQLAlchemy.ipynb)
* [Streamlit](https://github.com/streamlit/streamlit): Streamlit lets you transform Python scripts into interactive web apps in minutes, instead of weeks. Build dashboards, generate reports, or create chat apps.

## Queue
* [Celery](./Celery.md): Distributed Task Queue.
* [RQ](https://github.com/rq/rq): RQ (Redis Queue) is a simple Python library for queueing jobs and processing them in the background with workers. It is backed by Redis and it is designed to have a low barrier to entry. It can be integrated in your web stack easily.

## Server
* [gevent](https://github.com/gevent/gevent): gevent is a coroutine-based Python networking library that uses *greenlet* to provide a high-level synchronous API on top of the *libev* or *libuv* event loop.
* [GRPC](./grpc.ipynb)
* [gunicorn](https://github.com/benoitc/gunicorn): Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model ported from Ruby's Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy.
* [HTTPX](https://www.python-httpx.org/): HTTPX is a fully featured HTTP client for Python 3, which provides sync and async APIs, and support for both HTTP/1.1 and HTTP/2.
* [mod_wsgi](https://github.com/GrahamDumpleton/mod_wsgi): The mod_wsgi package provides an Apache module that implements a WSGI compliant interface for hosting Python based web applications on top of the Apache web server.
* [NGINX Unit](https://unit.nginx.org/): NGINX Unit is a lightweight and versatile application runtime that provides the essential components for your web application as a single open-source server: running application code (including WebAssembly), serving static assets, handling TLS and request routing.
* [Pika](./pika.ipynb): Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that tries to stay fairly independent of the underlying network support library.
* [ProtoBuf](./protobuf.ipynb)
* [Requests: HTTP for Humans™](https://docs.python-requests.org/en/latest/): Requests is an elegant and simple HTTP library for Python, built for human beings.
* [Starlette](https://www.starlette.io/): Starlette is a lightweight ASGI framework/toolkit, which is ideal for building async web services in Python.
* [Tornado](https://github.com/tornadoweb/tornado): Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed.
* [Twisted](https://github.com/twisted/twisted): Event-driven networking engine written in Python.
* [Uvicorn](./Uvicorn.md)
* [uWSGI](https://github.com/unbit/uwsgi/): The uWSGI project aims at developing a full stack for building hosting services. Application servers (for various programming languages and protocols), proxies, process managers and monitors are all implemented using a common api and a common configuration style.
* [WebSockets](./websockets.ipynb)
* [WSGI](./wsgi.ipynb)

## Misc
* [attrs](https://www.attrs.org/): attrs is the Python package that will bring back the joy of writing classes by relieving you from the drudgery of implementing object protocols (aka dunder methods). Trusted by NASA for Mars missions since 2020! - “Dunder” is a contraction of “double underscore”.
* [Pillow](https://pypi.org/project/pillow/): Python Imaging Library (Fork).
* [pyedflib](https://github.com/holgern/pyedflib): a python library to read/write EDF+/BDF+ files based on EDFlib.
* [Python Tutor](https://pythontutor.com/): Online Compiler, AI Tutor, and Visual Debugger for Python, Java, C, C++, and JavaScript.
* [Regular Expression](./Regular%20Expression.ipynb)
* [Rich](https://github.com/Textualize/rich): Rich is a Python library for rich text and beautiful formatting in the terminal.
* [Scrapy](https://scrapy.org/): A Fast and Powerful Scraping and Web Crawling Framework
* [tqdm](./tqdm.ipynb): A Fast, Extensible Progress Bar for Python and CLI.

# Installation and Upgrade

MacOS: `pyenv`.

Ubuntu:
```shell
# upgrage in Ubuntu
# https://cloudbytes.dev/snippets/upgrade-python-to-latest-version-on-ubuntu-linux
sudo apt update && sudo apt upgrade -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

apt list | grep python3.12
sudo apt install python3.12


sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1 
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 2
sudo update-alternatives --config python3

echo "alias python=/usr/bin/python3.12" >> ~/.bashrc

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3.12 get-pip.py
```
