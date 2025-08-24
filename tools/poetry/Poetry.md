# Poetry
* https://python-poetry.org/

> Poetry: Python packaging and dependency management made easy
>
> Poetry helps you declare, manage and install dependencies of Python projects, ensuring you have the right stack everywhere.
>
> Poetry replaces `setup.py`, `requirements.txt`, `setup.cfg`, `MANIFEST.in` and Pipfile with a simple `pyproject.toml` based project format.

> Poetry is a tool for dependency management**dependency management** and **packaging** in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. Poetry offers a lockfile to ensure repeatable installs, and can build your project for distribution.

```shell
$ pipx install poetry
$ poetry --version
Poetry (version 2.1.4)
```

# Basic usage
* https://python-poetry.org/docs/basic-usage/

```shell
# create new project
$ poetry new poetry-sample
Created package poetry_sample in poetry-sample
# or init an existing project: create pyproject.toml
$ poetry init

$ cd poetry-sample

# add dependency
$ poetry add pendulum
Creating virtualenv poetry-sample-E5coyubn-py3.12 in ~/AppData/Local/pypoetry/Cache/virtualenvs
Using version ^3.1.0 for pendulum

Updating dependencies
Resolving dependencies... (8.5s)

Package operations: 4 installs, 0 updates, 0 removals

  - Installing six (1.17.0)
  - Installing python-dateutil (2.9.0.post0)
  - Installing tzdata (2025.2)
  - Installing pendulum (3.1.0)

Writing lock file

# run
$ poetry run which python
~/AppData/Local/pypoetry/Cache/virtualenvs/poetry-sample-E5coyubn-py3.12/Scripts/python
$ poetry run python src/main.py 
Hello poetry_sample
```

# Managing dependencies
* https://python-poetry.org/docs/managing-dependencies/

PEP 621 – Storing project metadata in pyproject.toml

Poetry provides a way to organize your dependencies by **groups**.

```shell
poetry add pytest --group test
```

# Commands
* https://python-poetry.org/docs/cli/

# Configuration
* https://python-poetry.org/docs/configuration
  * Default Directories

`config.toml`: `config` command, 
- windows `%APPDATA%\pypoetry`, UNIX `~/.config/pypoetry`

`poetry.toml`: local configuration `config --local`

# The pyproject.toml file
* https://python-poetry.org/docs/pyproject/

sections:
- `project`: The project section of the pyproject.toml file according to the specification of the PyPA.
- `tool.poetry`: The tool.poetry section of the pyproject.toml file is composed of multiple sections.
- `build-system`: PEP-517 introduces a standard way to define alternative build systems to build a Python project.

# Dependency specification
* https://python-poetry.org/docs/dependency-specification/

# Managing environments
* https://python-poetry.org/docs/managing-environments/

```shell
# Displaying the environment information
$ poetry env info

# Listing the environments associated with the project
$ poetry env list

# Activating the environment
$ eval $(poetry env activate)
You must source this script: $ source ~\AppData\Local\pypoetry\Cache\virtualenvs\poetry-sample-E5coyubn-py3.12\Scripts\activate   
$ source ~/AppData/Local/pypoetry/Cache/virtualenvs/poetry-sample-E5coyubn-py3.12/Scripts/activate
(poetry-sample-py3.12) $   
```

```shell
# https://github.com/python-poetry/poetry-plugin-shell
$ poetry self add poetry-plugin-shell
# run a subshell with virtual environment activated
$ poetry shell
Spawning shell within ~\AppData\Local\pypoetry\Cache\virtualenvs\poetry-sample-E5coyubn-py3.12
```

more:
```shell
# Switching between environments
poetry env use /full/path/to/python

poetry env use python3.7
poetry env use 3.7

poetry env use system

# Deleting the environments
poetry env remove /full/path/to/python
poetry env remove python3.7
poetry env remove 3.7
poetry env remove test-O3eWbxRl-py3.7

poetry env remove python3.6 python3.7 python3.8

poetry env remove --all
```

Create the virtualenv inside the project’s root directory:
```shell
# (1) local
# https://python-poetry.org/docs/configuration/#virtualenvsin-project
# will create poetry.toml
$ poetry config virtualenvs.in-project true --local
# (2) global
# ~\AppData\Roaming\pypoetry\config.toml
$ poetry config --list
$ poetry config virtualenvs.in-project true

# then activate the environment
$ eval $(poetry env activate)
Creating virtualenv poetry-sample in D:\workspace\github\learning-python\tools\poetry\poetry-sample\.venv
You must source this script: $ source D:\workspace\github\learning-python\tools\poetry\poetry-sample\.venv\Scripts\activate
$ source .venv/Scripts/activate
(poetry-sample-py3.12) $
```

# VSCode extension
- [Python Poetry](https://github.com/zeshuaro/vscode-poetry)
- [Even Better TOML](https://github.com/tamasfe/taplo)