# Jupyter
* https://jupyter.org/

> Project Jupyter is a non-profit, open-source project, born out of the IPython in 2014 as it evolved to support interactive data science and scientific computing across all programming languages. Jupyter will always be 100% open-source software, free for all to use and released under the liberal terms of the modified BSD license.


# Installation

```shell
# https://pypi.org/project/jupyter
$ pip install jupyter
```

# Kernels

## BeakerX: Beaker extensions for Jupyter

* [Code](https://github.com/twosigma/beakerx)

BeakerX is a collection of JVM kernels and interactive widgets for plotting, tables, autotranslation, and other extensions to Jupyter Notebook and Jupyter Lab version 1.2.x and 2.x.

Latest release: 1.3.0, 2018-12-05.

```shell
$ pip install beakerx
$ beakerx install

# with docker: 7.66 GB, 6 years ago
$ docker run -itd -p 8888:8888 beakerx/beakerx
```

## C

* https://github.com/adamtuft/c-kernel
* https://github.com/XaverKlemenschits/jupyter-c-kernel
* https://github.com/shiroinekotfs/jupyter-cpp-kernel

## Common Lisp

* [cl-jupyter](https://github.com/fredokun/cl-jupyter) - latest version 2018-11-20
* [common-lisp-jupyter](https://github.com/yitzchak/common-lisp-jupyter) - latest version 2024-10

MacOS:

```shell
$ brew install zmq

# alternative
# build source of zeromq-4.3.5.tar.gz
./configure
make install
# add zmq.h to clang search path for /Users/zhang/.cache/common-lisp/sbcl-2.4.7-macosx-x64/Users/zhang/quicklisp/dists/quicklisp/software/pzmq-20210531-git
export CPATH=/usr/local/include

touch /Users/zhang/Library/common-lisp-jupyter/image
```

```lisp
(ql:quickload :common-lisp-jupyter)
(cl-jupyter:install)
Installing kernel spec file /Users/zhang/Library/Jupyter/kernels/common-lisp/kernel.json
Installing kernel resources to /Users/zhang/Library/Jupyter/kernels/common-lisp/.

(cl-jupyter:install-image)
Creating directories.
Installing kernel spec file /Users/zhang/Library/Jupyter/kernels/common-lisp/kernel.json
Installing kernel resources to /Users/zhang/Library/Jupyter/kernels/common-lisp/.
Creating kernel image /Users/zhang/Library/common-lisp-jupyter/image
[undoing binding stack and other enclosing state... done]
[performing final GC... done]
[defragmenting immobile space... (inst,code,sym)=1660+27255+32651... done]
[saving current Lisp image into /Users/zhang/Library/common-lisp-jupyter/image:
writing 98304 bytes from the linkage space at 0xb7ffc00000
writing 3232 bytes from the static space at 0x50000000
writing 29392896 bytes from the dynamic space at 0x1000000000
writing 10424320 bytes from the read-only space at 0xfff608000
writing 1781760 bytes from the fixedobj space at 0x50900000
writing 17010688 bytes from the text space at 0xb800000000
done]
```

```shell
# console mode
➜  ~ jupyter console --kernel=common-lisp


Jupyter console 6.6.3

common-lisp-jupyter: a Common Lisp Jupyter kernel
(C) 2019-2020 Tarn Burton (MIT)
In [1]: (+ 1 2)
Out[1]: 3

# Notebook mode
jupyter lab
```

Windows: with [[Miniconda]]

* [link](https://github.com/yitzchak/common-lisp-jupyter/wiki/Windows-Installation)

```shell
conda install -c conda-forge jupyterlab jupyter_console m2w64-gcc m2w64-zeromq
```

```lisp
(ql:quickload :common-lisp-jupyter)
(cl-jupyter:install)
```

```shell
jupyter-labextension install jupyterlab-debugger-restarts
```

## Go

* [gophernotes](https://github.com/gopherdata/gophernotes): The Go kernel for Jupyter notebooks and nteract. - latest version 0.7.5 2022-06-01
* [GoNB](https://github.com/janpfeifer/gonb) - latest version 0.10.6 2024-10
** [tutorial](https://github.com/janpfeifer/gonb/blob/main/examples/tutorial.ipynb)
** Windows: use WSL `~/.local/share/jupyter/kernels/gonb/kernel.json`
** MacOS

## Haskell

* [IHaskell](https://github.com/IHaskell/IHaskell): A Haskell kernel for the Jupyter project.

## Java

* [Ganymede](https://github.com/allen-ball/ganymede): The Ganymede Kernel is a Jupyter Notebook Java kernel based on the Java Shell tool, JShell.
* [JJava](https://github.com/dflib/jjava): JJava is an evolution of the earlier IJava kernel, that is no longer maintained by its authors.

## OCaml

* [OCaml Jupyter](https://github.com/akabe/ocaml-jupyter): An OCaml kernel for Jupyter (IPython) notebook

```shell
# windows WSL
/home/zhoujiagen/.local/share/jupyter/kernels/ocaml-jupyter-default
```


## Rust

* [Evcxr](https://github.com/evcxr/evcxr)

## Scala

* [almond](https://github.com/almond-sh/almond): A Scala kernel for Jupyter

Action: `jupyter-notebooks/Scala/_almond.ipynb`

```shell
$ cs launch --use-bootstrap almond -- --install
# windows
Installed scala kernel under ~/AppData/Roaming/jupyter/kernels/scala
```

## SQL

* [JupySQL](https://github.com/ploomber/jupysql): Run SQL in Jupyter/IPython via a `%sql` and `%%sql` magics.

```shell
pip install jupysql
# https://github.com/PyMySQL/mysqlclient
pip install mysqlclient
```

```python
%load_ext sql
#%load_ext sql

%sql mysql+mysqldb://root:xxx!@localhost:3306/db1

%sqlcmd tables
%sqlcmd tables --schema db1
%sqlcmd columns --table table1 --schema db1

%%sql
SELECT * FROM db1.table1;
```

# Themes

* [link](https://github.com/dunovank/jupyter-themes)

```shell
pip install jupyterthemes
jt -l
jt -t chesterish -f ubuntu -nf ubuntu -tf ubuntu -fs 13 -nfs 13 -ofs 12 -tfs 12 -lineh 150 -T -kl

jt -r
Reset css and font defaults in:
~/.jupyter/custom &
xxx/jupyter/nbextensions
```

`~/.jupyter/custom/custom.css`:

```css
div.output_subarea {
  ...
  padding: 0em !important;
  ...
}

pre {
    font-family: 'Ubuntu Mono';
    font-size: 13px;
}

div.CodeMirror-code {
    font-family: 'Ubuntu Mono';
    font-size: 15px;
}

div.cell, div.input_area, div.CodeMirror-gutter.CodeMirror-foldgutter, div.CodeMirror-gutter.CodeMirror-linenumbers {
    background-color: #E3EDCD;
}

div.output_subarea {
    background-color: #2F4F4F;
    font-size: 13px;
}

div.output_subarea pre {
    color: lightgreen;
}

div#toc-wrapper {
    top: 55px;
    background-color: #E3EDCD;
}

div#notebook-container {
    background-color: #E3EDCD;
}

table {
    background-color: lightblue;
}

div p {
    color: lightgreen;
}
```

# jupyter-black: formatter

* [link](https://github.com/drillan/jupyter-black)

```shell
pip install black
jupyter nbextension install https://github.com/drillan/jupyter-black/archive/master.zip --user
jupyter nbextension enable jupyter-black-master/jupyter-black
```

# jupyter_contrib_nbextensions

* [link](https://github.com/ipython-contrib/jupyter_contrib_nbextensions)

```shell
pip install jupyter_contrib_nbextensions
// conda install -c conda-forge jupyter_contrib_nbextensions

jupyter nbextension enable <nbextension require path>
jupyter nbextension disable <nbextension require path>
```

# Paths: Config, Data, Runtime

* [link](https://docs.jupyter.org/en/latest/use/jupyter-directories.html)

Windows:

```shell
    jupyter --paths                                                                                          
    config:
        ~\.jupyter
        ~\AppData\Roaming\Python\etc\jupyter
        C:\Python311\etc\jupyter
        C:\ProgramData\jupyter
    data:
        ~\AppData\Roaming\jupyter
        ~\AppData\Roaming\Python\share\jupyter
        C:\Python311\share\jupyter
        C:\ProgramData\jupyter
    runtime:
        ~\AppData\Roaming\jupyter\runtime


# Common Lisp, Rust
~\AppData\Roaming\jupyter\kernels

```

# Input

* [How to give jupyter cell standard input in python?](https://stackoverflow.com/questions/34968112/how-to-give-jupyter-cell-standard-input-in-python)

```python
a = intput("prompt")
print(a)
```

# Jupyter Book

* [Jupyter Book](https://jupyterbook.org/en/stable/intro.html): Build beautiful, publication-quality books and documents from computational content.
** [Gallery of Jupyter Books](https://executablebooks.org/en/latest/gallery/`)

## Docs
| Topics                                                                                                      | Description                                              |h
|[Get started with Jupyter Notebook](https://docs.jupyter.org/en/latest/start/index.html)                    |Try the notebook                                         |
|[Architecture](https://docs.jupyter.org/en/latest/projects/architecture/content-architecture.html)          |What is Jupyter?                                         |
|[Narratives and Use Cases](https://docs.jupyter.org/en/latest/use/use-cases/content-user.html)              |Narratives of common deployment scenarios                |
|[IPython](https://docs.jupyter.org/en/latest/reference/ipython.html)                                        |An interactive Python kernel and REPL                    |
|[Installation, Configuration, and Usage](https://docs.jupyter.org/en/latest/projects/content-projects.html) |Documentation for users                                  |
|[Community](https://docs.jupyter.org/en/latest/community/content-community.html)                            |Sustainability and growth                                |
|[Contributor Guides](https://docs.jupyter.org/en/latest/contributing/content-contributor.html)              |How to contribute to the projects                        |
|[Release Notes](https://docs.jupyter.org/en/latest/releases.html)                                           |New features, upgrades, deprecation notes, and bug fixes |
|[Reference](https://docs.jupyter.org/en/latest/reference/content-reference.html)                            |APIs                                                     |
|[Advanced](https://docs.jupyter.org/en/latest/use/advanced/content-advanced.html)                           |Documentation for advanced use-cases                     |

# Jupyter Kernels


## Kernel specs

files:

* `kernel.json`
* `kernel.js`
* logo image file.

list and usages:

```shell
$ jupyter kernelspec list

$ jupyter console --kernel bash
$ jupyter qtconsole --kernel bash
```

### Example `kernel.json`

Rust Evcxr:

```json
{
  "argv": [
    "D:\\rust\\.cargo\\bin\\evcxr_jupyter.exe",
    "--control_file",
    "{connection_file}"
  ],
  "display_name": "Rust",
  "language": "rust",
  "interrupt_mode": "message"
}
```

common-lisp-jupyter:

```json
{
  "argv": [
    "D:\\software\\SBCL-2.4.10\\sbcl.exe",
    "--eval",
    "(ql:quickload :common-lisp-jupyter)",
    "--eval",
    "(jupyter:run-kernel 'jupyter/common-lisp:kernel)",
    "{connection_file}"
  ],
  "display_name": "Common Lisp",
  "language": "common-lisp",
  "interrupt_mode": "message",
  "metadata": {
    "debugger": true
  }
}
```

## ZeroMQ based Messaging

design diagram: [img[https://github.com/jupyter/jupyter_client/blob/main/docs/figs/frontend-kernel.png?raw=true]]

socket channels:

* ''Shell'': requests for code execution, object information, prompts, etc.
* ''IOPub'': the ‘broadcast channel’.
* ''stdin'': request input from the active frontend when `raw_input()` is called.
* ''Control'': use for shutdown/restart/debugging messages.
* ''Heartbeat'': connection liveness among frontend and kernel.

example: [[simple_kernel.py|https://github.com/dsblank/simple_kernel/blob/master/simple_kernel.py]]

## References

* [[Jupyter kernels|https://github.com/jupyter/jupyter/wiki/Jupyter-kernels]]

> Kernel Zero is [[IPython|https://ipython.org/]], which you can get through [[ipykernel|https://pypi.python.org/pypi/ipykernel]], and is still a dependency of [[jupyter|https://jupyter.org/]]. The IPython kernel can be thought of as a reference implementation, as CPython is for Python.

* [[Making kernels for Jupyter|https://jupyter-client.readthedocs.io/en/latest/kernels.html]]
* [[Messaging in Jupyter|https://jupyter-client.readthedocs.io/en/latest/index.html]]

* [[Manage Jupyter Kernels in VS Code|https://code.visualstudio.com/docs/datascience/jupyter-kernel-management]]