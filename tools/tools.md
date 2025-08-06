
# Python Tools

## Skafold
* [cookiecutter](./cookiecutter/cookiecutter.md)
* [PyScaffold](./PyScaffold.md)

## Environment
* [click](https://github.com/pallets/click): Python composable command line interface toolkit.
* [IPython](./IPython.md)
  * [ipython.ipynb](./ipython.ipynb)
  * [ipython_magics.ipynb](./ipython_magics.ipynb)
  * [KaTeX.ipynb](./KaTeX.ipynb)
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
* [pydoc](./pydoc.md)
* [Setuptools](https://setuptools.pypa.io/en/latest/userguide/index.html): Setuptools is a fully-featured, actively-maintained, and stable library designed to facilitate packaging Python projects. It helps developers to easily share reusable code (in the form of a library) and programs (e.g., CLI/GUI tools implemented in Python), that can be installed with pip and uploaded to PyPI.
* [tox](./tox.md): tox aims to automate and standardize testing in Python.
* [uv](./uv.md): An extremely fast Python package and project manager, written in Rust.

## Template
* [Jinja](./Jinja.md): Jinja is a fast, expressive, extensible templating engine

## Linter, Formatter, Type Checker
* [autopep8](https://pypi.org/project/autopep8/): autopep8 automatically formats Python code to conform to the PEP 8 style guide. It uses the pycodestyle utility to determine what parts of the code needs to be formatted. autopep8 is capable of fixing most of the formatting issues that can be reported by pycodestyle.
* [Black](./Black.md): The uncompromising code formatter.
* [flake8](http://flake8.pycqa.org/en/latest/index.html): flake8 is a python tool that glues together pycodestyle, pyflakes, mccabe, and third-party plugins to check the style and quality of some python code.
* [mypy](https://mypy-lang.org/): Mypy is an optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing and static typing. Mypy combines the expressive power and convenience of Python with a powerful type system and compile-time type checking. Mypy type checks standard Python programs; run them using any Python VM with basically no runtime overhead.
* [pycodestyle.md](./pycodestyle.md)
* [Pylint](https://pylint.readthedocs.io/en/latest/index.html): Pylint is a static code analyser for Python 2 or 3. The latest version supports Python 3.8.0 and above. Pylint analyses your code without actually running it. It checks for errors, enforces a coding standard, looks for code smells, and can make suggestions about how the code could be refactored.

## Testing
* [Coverage.py](https://github.com/nedbat/coveragepy): Code coverage measurement for Python.
* [Faker](./Faker.md): Faker is a Python package that generates fake data for you.
* [mock](https://mock.readthedocs.io/en/latest/): mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used. mock is now part of the Python standard library, available as `unittest.mock` in Python 3.3 onwards.
* [Playwright](https://github.com/microsoft/playwright): Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API.
* [pytest](./pytest.md): The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.
* [Selenium](https://github.com/SeleniumHQ/selenium): A browser automation framework and ecosystem.

## Logging
* [logging](https://docs.python.org/3/library/logging.html): Logging facility for Python.
  * [LogRecord attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes)
* [python-json-logger](https://github.com/nhairs/python-json-logger): Python JSON Logger enables you produce JSON logs when using Python's `logging` package.

## Database
* [JupySQL](./JupySQL.ipynb) 
* [Pydantic](https://docs.pydantic.dev/): Pydantic is the most widely used data validation library for Python.
* [PyMySQL](./PyMySQL.ipynb)
* [SQLAlchemy](./SQLAlchemy.ipynb)

## Server
* [GRPC](./grpc.ipynb)
* [HTTPX](https://www.python-httpx.org/): HTTPX is a fully featured HTTP client for Python 3, which provides sync and async APIs, and support for both HTTP/1.1 and HTTP/2.
* [Pika](./pika.ipynb) 
* [ProtoBuf](./protobuf.ipynb)
* [Requests: HTTP for Humans™](https://docs.python-requests.org/en/latest/): Requests is an elegant and simple HTTP library for Python, built for human beings.
* [Starlette](https://www.starlette.io/): Starlette is a lightweight ASGI framework/toolkit, which is ideal for building async web services in Python.
* [Twisted](https://github.com/twisted/twisted): Event-driven networking engine written in Python.
* [Uvicorn](./Uvicorn.md)
* [WebSockets](./websockets.ipynb)
* [WSGI](./wsgi.ipynb)

## Misc
* [attrs](https://www.attrs.org/): attrs is the Python package that will bring back the joy of writing classes by relieving you from the drudgery of implementing object protocols (aka dunder methods). Trusted by NASA for Mars missions since 2020! - “Dunder” is a contraction of “double underscore”.
* [Regular Expression](./Regular%20Expression.ipynb)
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

## More
* [pyedflib](https://github.com/holgern/pyedflib): a python library to read/write EDF+/BDF+ files based on EDFlib.
* [Scrapy](https://scrapy.org/): A Fast and Powerful Scraping and Web Crawling Framework