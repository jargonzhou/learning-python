# Test interactive Python examples

```shell
# python -m doctest [-v] [-o OPTION] [-f] file [file ...]
python Module.py -v
```

```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()

doctest.testfile("example.text")
```