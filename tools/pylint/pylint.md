# pylint
* https://pylint.readthedocs.io/en/latest/index.html
* [Pylint extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)

> Pylint is a static code analyser for Python 2 or 3. The latest version supports Python 3.8.0 and above. Pylint analyses your code without actually running it. It checks for errors, enforces a coding standard, looks for code smells, and can make suggestions about how the code could be refactored.

```shell
$ pip install pylint
```

# Messages
* https://pylint.readthedocs.io/en/latest/user_guide/messages/index.html
* Disabling messages: [Messages control](https://pylint.readthedocs.io/en/latest/user_guide/messages/message_control.html)

Messages categories
- Fatal
- Error
- Warning
- Convention
- Refactor
- Information

```python
# skip entire file:
# pylint: skip-file

# skip specific checks:
# pylint: disable=missing-class-docstring,missing-function-docstring
```

# pyreverse
* https://pylint.readthedocs.io/en/latest/additional_tools/pyreverse/configuration.html

> standalone tool that generates package and class diagrams.


```shell
# pyreverse [options] <packages>

# This module implements specialized container datatypes providing alternatives to Python's general purpose built-in containers, dict, list, set, and tuple.
pyreverse --filter-mode ALL --show-stdlib --show-builtin  collections --output html

# Abstract Base Classes (ABCs) for collections, according to PEP 3119.
pyreverse --filter-mode ALL --show-stdlib --show-builtin _collections_abc --output html
```
