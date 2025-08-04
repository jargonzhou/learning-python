# pydoc
* https://docs.python.org/3/library/pydoc.html
* [Documenting Python Code: A Complete Guide](https://realpython.com/documenting-python-code/)

> pydoc — Documentation generator and online help system
>
> The pydoc module automatically generates documentation from Python modules. The documentation can be presented as pages of text on the console, served to a web browser, or saved to HTML files.

## Usage

```shell
# run with a search gui
pydoc -g 
	
# or define a port
pydoc -p 8888

# gen doc
pydoc -w com/spike/hello/*
```