
# Python Tools

* [attrs](https://www.attrs.org/): attrs is the Python package that will bring back the joy of writing classes by relieving you from the drudgery of implementing object protocols (aka dunder methods). Trusted by NASA for Mars missions since 2020! - “Dunder” is a contraction of “double underscore”.
* [Black](./Black.md)
* [Faker](./Faker.md)
* [flake8](http://flake8.pycqa.org/en/latest/index.html): flake8 is a python tool that glues together pycodestyle, pyflakes, mccabe, and third-party plugins to check the style and quality of some python code.
* [GRPC](./grpc.ipynb)
* [HTTPX](https://www.python-httpx.org/): HTTPX is a fully featured HTTP client for Python 3, which provides sync and async APIs, and support for both HTTP/1.1 and HTTP/2.
* [IPython](./IPython.md)
  * [ipython.ipynb](./ipython.ipynb)
  * [ipython_magics.ipynb](./ipython_magics.ipynb)
  * [KaTeX.ipynb](./KaTeX.ipynb)
* [Jinja](./Jinja.md) 
* [JupySQL](./JupySQL.ipynb) 
* [Miniconda](https://docs.anaconda.com/miniconda/):  Miniconda is a free, miniature installation of Anaconda Distribution that includes only conda, Python, the packages they both depend on, and a small number of other useful packages.
* [mock](https://mock.readthedocs.io/en/latest/): mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used. mock is now part of the Python standard library, available as `unittest.mock` in Python 3.3 onwards.
* [mypy](https://mypy-lang.org/): Mypy is an optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing and static typing. Mypy combines the expressive power and convenience of Python with a powerful type system and compile-time type checking. Mypy type checks standard Python programs; run them using any Python VM with basically no runtime overhead.
* [Pika](./pika.ipynb) 
* [pip.md](./pip.md)
* [Pipenv.md](./Pipenv.md)
* [Poetry](./Poetry.md)
* [ProtoBuf](./protobuf.ipynb)
* [pycodestyle.md](./pycodestyle.md)
* [Pydantic](https://docs.pydantic.dev/): Pydantic is the most widely used data validation library for Python.
* [PyDoc.md](./PyDoc.md)
* [pyenv](https://github.com/pyenv/pyenv): pyenv lets you easily switch between multiple versions of Python. It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.
* [Pylint](https://pylint.readthedocs.io/en/latest/index.html): Pylint is a static code analyser for Python 2 or 3. The latest version supports Python 3.8.0 and above. Pylint analyses your code without actually running it. It checks for errors, enforces a coding standard, looks for code smells, and can make suggestions about how the code could be refactored.
* [PyMySQL](./PyMySQL.ipynb)
* [pytest](./pytest.md)
* [Python Tutor](https://pythontutor.com/): Online Compiler, Visual Debugger, and AI Tutor for Python, Java, C, C++, and JavaScript
* [Regular Expression](./Regular%20Expression.ipynb)
* [Requests: HTTP for Humans™](https://docs.python-requests.org/en/latest/): Requests is an elegant and simple HTTP library for Python, built for human beings.
* [Setuptools](https://setuptools.pypa.io/en/latest/userguide/index.html): Setuptools is a fully-featured, actively-maintained, and stable library designed to facilitate packaging Python projects. It helps developers to easily share reusable code (in the form of a library) and programs (e.g., CLI/GUI tools implemented in Python), that can be installed with pip and uploaded to PyPI.
* [SQLAlchemy](./SQLAlchemy.ipynb)
* [Starlette](https://www.starlette.io/): Starlette is a lightweight ASGI framework/toolkit, which is ideal for building async web services in Python.
* [tqdm](./tqdm.ipynb)
* [Twisted](https://github.com/twisted/twisted): Event-driven networking engine written in Python.
* [uv](./uv.md)
* [Uvicorn](./Uvicorn.md)
* [virtualenv](./virtualenv.md)
* [WebSockets](./websockets.ipynb)
* [WSGI](./wsgi.ipynb)


## Installation and Upgrade

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