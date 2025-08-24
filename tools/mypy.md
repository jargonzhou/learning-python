# mypy
* https://mypy-lang.org/
* [vscode-mypy](https://github.com/microsoft/vscode-mypy)

> Mypy is an optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing and static typing. Mypy combines the expressive power and convenience of Python with a powerful type system and compile-time type checking. Mypy type checks standard Python programs; run them using any Python VM with basically no runtime overhead.

# FAQ

- ignore errors
https://mypy.readthedocs.io/en/stable/common_issues.html#ignoring-a-whole-file
```python
# top level:
# mypy: ignore-errors
# module:
# type: ignore
# inline:
# type: ignore[<code>]

# specific error code
# mypy: disable-error-code="truthy-bool, ignore-without-code"

# replace contents of a module with Any: configuration
follow_imports = skip
```