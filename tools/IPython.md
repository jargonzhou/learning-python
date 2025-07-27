# IPython
* https://ipython.org/
* [ipykernel](https://ipython.readthedocs.io/en/stable/)
* [ipyparallel](https://ipyparallel.readthedocs.io/en/latest/)
* [traitlets](https://traitlets.readthedocs.io/en/stable/)

> IPython provides a rich toolkit to help you make the most of using Python interactively. Its main components are:
>
> * A powerful interactive Python shell.
> * A Jupyter kernel to work with Python code in Jupyter notebooks and other interactive frontends.

# Installation

MacOS:

```shell
➜  ~ pip --version
pip 23.3 from /usr/local/lib/python3.11/site-packages/pip (python 3.11)
➜  ~ pip list | grep ipy
ipykernel                  6.29.5
ipython                    8.28.0
ipywidgets                 8.1.5

➜  ~ ipython
Python 3.11.3 (main, Apr 27 2023, 15:01:20) [Clang 12.0.0 (clang-1200.0.32.21)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.28.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 42
Out[1]: 42

In [2]: ?

In [3]: %quickref

In [4]: exit
```

# Built-in magic commands

* [link](https://ipython.readthedocs.io/en/stable/interactive/magics.html)

```python
!lsmagic
```

| Command           | Scope | Scope 2         | Description                                                                            |h
| `alias`           | Line  | OSMagics        |                                                                                        |
| `alias_magic`     | Line  | BasicMagics     |                                                                                        |
| `autoawait`       | Line  | AsyncMagics     |                                                                                        |
| `autocall`        | Line  | AutoMagics      |                                                                                        |
| `automagic`       | Line  | AutoMagics      |                                                                                        |
| `autosave`        | Line  | KernelMagics    |                                                                                        |
| `bookmark`        | Line  | OSMagics        |                                                                                        |
| `cat`             | Line  | Other           |                                                                                        |
| `cd`              | Line  | OSMagics        |                                                                                        |
| `clear`           | Line  | KernelMagics    |                                                                                        |
| `code_wrap`       | Line  | ExecutionMagics |                                                                                        |
| `colors`          | Line  | BasicMagics     |                                                                                        |
| `conda`           | Line  | PackagingMagics |                                                                                        |
| `config`          | Line  | ConfigMagics    |                                                                                        |
| `connect_info`    | Line  | KernelMagics    |                                                                                        |
| `cp`              | Line  | Other           |                                                                                        |
| `debug`           | Line  | ExecutionMagics |                                                                                        |
| `dhist`           | Line  | OSMagics        |                                                                                        |
| `dirs`            | Line  | OSMagics        |                                                                                        |
| `doctest_mode`    | Line  | BasicMagics     |                                                                                        |
| `ed`              | Line  | Other           |                                                                                        |
| `edit`            | Line  | KernelMagics    |                                                                                        |
| `env`             | Line  | OSMagics        |                                                                                        |
| `gui`             | Line  | BasicMagics     |                                                                                        |
| `hist`            | Line  | Other           |                                                                                        |
| `history`         | Line  | HistoryMagics   |                                                                                        |
| `killbgscripts`   | Line  | ScriptMagics    |                                                                                        |
| `ldir`            | Line  | Other           |                                                                                        |
| `less`            | Line  | KernelMagics    |                                                                                        |
| `lf`              | Line  | Other           |                                                                                        |
| `lk`              | Line  | Other           |                                                                                        |
| `ll`              | Line  | Other           |                                                                                        |
| `load`            | Line  | CodeMagics      |                                                                                        |
| `load_ext`        | Line  | ExtensionMagics |                                                                                        |
| `loadpy`          | Line  | CodeMagics      |                                                                                        |
| `logoff`          | Line  | LoggingMagics   |                                                                                        |
| `logon`           | Line  | LoggingMagics   |                                                                                        |
| `logstart`        | Line  | LoggingMagics   |                                                                                        |
| `logstate`        | Line  | LoggingMagics   |                                                                                        |
| `logstop`         | Line  | LoggingMagics   |                                                                                        |
| `ls`              | Line  | Other           |                                                                                        |
| `lsmagic`         | Line  | BasicMagics     |                                                                                        |
| `lx`              | Line  | Other           |                                                                                        |
| `macro`           | Line  | ExecutionMagics |                                                                                        |
| `magic`           | Line  | BasicMagics     |                                                                                        |
| `mamba`           | Line  | PackagingMagics |                                                                                        |
| `man`             | Line  | KernelMagics    |                                                                                        |
| `matplotlib`      | Line  | PylabMagics     |                                                                                        |
| `micromamba`      | Line  | PackagingMagics |                                                                                        |
| `mkdir`           | Line  | Other           |                                                                                        |
| `more`            | Line  | KernelMagics    |                                                                                        |
| `mv`              | Line  | Other           |                                                                                        |
| `notebook`        | Line  | BasicMagics     |                                                                                        |
| `page`            | Line  | BasicMagics     |                                                                                        |
| `pastebin`        | Line  | CodeMagics      |                                                                                        |
| `pdb`             | Line  | ExecutionMagics |                                                                                        |
| `pdef`            | Line  | NamespaceMagics |                                                                                        |
| `pdoc`            | Line  | NamespaceMagics |                                                                                        |
| `pfile`           | Line  | NamespaceMagics |                                                                                        |
| `pinfo`           | Line  | NamespaceMagics |                                                                                        |
| `pinfo2`          | Line  | NamespaceMagics |                                                                                        |
| `pip`             | Line  | PackagingMagics |                                                                                        |
| `popd`            | Line  | OSMagics        |                                                                                        |
| `pprint`          | Line  | BasicMagics     |                                                                                        |
| `precision`       | Line  | BasicMagics     |                                                                                        |
| `prun`            | Line  | ExecutionMagics |                                                                                        |
| `psearch`         | Line  | NamespaceMagics |                                                                                        |
| `psource`         | Line  | NamespaceMagics |                                                                                        |
| `pushd`           | Line  | OSMagics        |                                                                                        |
| `pwd`             | Line  | OSMagics        |                                                                                        |
| `pycat`           | Line  | OSMagics        |                                                                                        |
| `pylab`           | Line  | PylabMagics     |                                                                                        |
| `qtconsole`       | Line  | KernelMagics    |                                                                                        |
| `quickref`        | Line  | BasicMagics     |                                                                                        |
| `recall`          | Line  | HistoryMagics   |                                                                                        |
| `rehashx`         | Line  | OSMagics        |                                                                                        |
| `reload_ext`      | Line  | ExtensionMagics |                                                                                        |
| `rep`             | Line  | Other           |                                                                                        |
| `rerun`           | Line  | HistoryMagics   |                                                                                        |
| `reset`           | Line  | NamespaceMagics |                                                                                        |
| `reset_selective` | Line  | NamespaceMagics |                                                                                        |
| `rm`              | Line  | Other           |                                                                                        |
| `rmdir`           | Line  | Other           |                                                                                        |
| `run`             | Line  | ExecutionMagics |                                                                                        |
| `save`            | Line  | CodeMagics      |                                                                                        |
| `sc`              | Line  | OSMagics        |                                                                                        |
| `set_env`         | Line  | OSMagics        |                                                                                        |
| `store`           | Line  | StoreMagics     |                                                                                        |
| `sx`              | Line  | OSMagics        |                                                                                        |
| `system`          | Line  | OSMagics        |                                                                                        |
| `tb`              | Line  | ExecutionMagics |                                                                                        |
| `time`            | Line  | ExecutionMagics |                                                                                        |
| `timeit`          | Line  | ExecutionMagics |                                                                                        |
| `unalias`         | Line  | OSMagics        |                                                                                        |
| `unload_ext`      | Line  | ExtensionMagics |                                                                                        |
| `who`             | Line  | NamespaceMagics |                                                                                        |
| `who_ls`          | Line  | NamespaceMagics |                                                                                        |
| `whos`            | Line  | NamespaceMagics |                                                                                        |
| `xdel`            | Line  | NamespaceMagics |                                                                                        |
| `xmode`           | Line  | BasicMagics     | Switch modes for the exception handlers: `Plain`, `Context`, `Verbose`, and `Minimal`. |
|                   |       |                 |                                                                                        |
| `!`               | Cell  | OSMagics        |                                                                                        |
| `HTML`            | Cell  | Other           |                                                                                        |
| `SVG`             | Cell  | Other           |                                                                                        |
| `bash`            | Cell  | Other           |                                                                                        |
| `capture`         | Cell  | ExecutionMagics |                                                                                        |
| `code_wrap`       | Cell  | ExecutionMagics |                                                                                        |
| `debug`           | Cell  | ExecutionMagics |                                                                                        |
| `file`            | Cell  | Other           |                                                                                        |
| `html`            | Cell  | DisplayMagics   |                                                                                        |
| `javascript`      | Cell  | DisplayMagics   |                                                                                        |
| `js`              | Cell  | DisplayMagics   |                                                                                        |
| `latex`           | Cell  | DisplayMagics   |                                                                                        |
| `markdown`        | Cell  | DisplayMagics   |                                                                                        |
| `perl`            | Cell  | Other           |                                                                                        |
| `prun`            | Cell  | ExecutionMagics |                                                                                        |
| `pypy`            | Cell  | Other           |                                                                                        |
| `python`          | Cell  | Other           |                                                                                        |
| `python2`         | Cell  | Other           |                                                                                        |
| `python3`         | Cell  | Other           |                                                                                        |
| `ruby`            | Cell  | Other           |                                                                                        |
| `script`          | Cell  | ScriptMagics    |                                                                                        |
| `sh`              | Cell  | Other           |                                                                                        |
| `svg`             | Cell  | DisplayMagics   |                                                                                        |
| `sx`              | Cell  | OSMagics        |                                                                                        |
| `system`          | Cell  | OSMagics        |                                                                                        |
| `time`            | Cell  | ExecutionMagics |                                                                                        |
| `timeit`          | Cell  | ExecutionMagics |                                                                                        |
| `writefile`       | Cell  | OSMagics       |                                                                                        |

# Configuration

profile: allow you to use IPython for different tasks, keeping separate config files and history for each one.

```shell
ipython profile create
# directory: ~/.ipython/profile_default
```

Startup files:
put `.py`, `.ipy` scripts in `~/.ipython/profile_default/startup/` directory.

    This is the IPython startup directory

    .py and .ipy files in this directory will be run *prior* to any code or files specified
    via the exec_lines or exec_files configurables whenever you load this profile.

    Files will be run in lexicographical order, so you can control the execution order of files
    with a prefix, e.g.::

```
00-first.py
50-middle.py
99-last.ipy
```

```shell
➜  startup cat 00-imports.py 
print("requests...")
import requests
print("json...")
import json

print("numpy...")
import numpy as np
print("matplotlib...")
import matplotlib.pyplot as plt
print("pandas...")
import pandas as pd
#import seaborn as sns
#import statsmodels as sm
```

# Configuration and customization

* [link](https://ipython.readthedocs.io/en/stable/config/index.html)

### Magics

* [Jupyter: trick to run next cell even if previous cell fails](https://stackoverflow.com/questions/57364510/jupyter-trick-to-run-next-cell-even-if-previous-cell-fails) - StackOverflow

```python
from IPython.core.magic import Magics, magics_class, cell_magic
@magics_class
@cell_magic

%load_ext
```

* [How to Skip Cell Execution in Jupyter Notebook](https://kioku-space.com/en/jupyter-skip-execution/)

```python
from IPython.core.magic import register_cell_magic
from IPython import get_ipython

eval(line)
get_ipython().run_cell(cell)
```

# Cookbook

* [link](https://github.com/ipython/ipython/wiki/Cookbook%3A-Index)

# Tips and Tricks

* [link](https://ipython.readthedocs.io/en/stable/interactive/tips.html#tips)

* [Running A Cell In A Background Thread](https://discourse.jupyter.org/t/running-a-cell-in-a-background-thread/12267/2): example `_ipython.ipynb`

* ["asyncio.run() cannot be called from a running event loop" when using Jupyter Notebook](https://stackoverflow.com/questions/55409641/asyncio-run-cannot-be-called-from-a-running-event-loop-when-using-jupyter-no): example `books/Fluent Python/19-Concurrency-Models-in-Python.ipynb`
