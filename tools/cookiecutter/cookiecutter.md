# cookiecutter
* https://github.com/cookiecutter/cookiecutter
* templates: https://github.com/search?q=cookiecutter&type=Repositories

> A cross-platform command-line utility that creates projects from cookiecutters (project templates), e.g. Python package projects, C projects.

```shell
$ pip install -U cookiecutter
```

# cookiecutter-pypackage
* https://github.com/audreyfeldroy/cookiecutter-pypackage

> Cookiecutter template for a Python package.

```shell
$ cookiecutter https://github.com/audreyfeldroy/cookiecutter-pypackage.git
  [1/9] full_name (Audrey M. Roy Greenfeld): jargonzhou
  [2/9] email (audreyfeldroy@example.com): zhoujiagen@gmail.com
  [3/9] github_username (audreyfeldroy): jargonzhou
  [4/9] pypi_package_name (python-boilerplate): python-sample
  [5/9] project_name (Python Boilerplate): python-sample
  [6/9] project_slug (python_sample): 
  [7/9] project_short_description (Python Boilerplate contains all the boilerplate you need to create a 
Python package.): 
  [8/9] pypi_username (jargonzhou): 
  [9/9] first_version (0.1.0): 
Your Python package project has been created successfully!

$ cd python-sample
$ source .venv/Scripts/activate
(python-sample-py3.12) $ poetry install

(python-sample-py3.12) $ poetry run python_sample
Replace this message by putting your code into python_sample.cli.main
See Typer documentation at https://typer.tiangolo.com/
Replace this with a utility function
```

debug: see [.vscode/launch.json](./python-sample/.vscode/launch.json)

test:
```shell
(python-sample-py3.12) $ poetry install --all-extras
(python-sample-py3.12) $ poetry run pytest
```