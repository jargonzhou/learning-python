# pipx
* (https://pipx.pypa.io 

> Install and Run Python Applications in Isolated Environments

```shell
$ pip install -U pipx
$ pipx --version
1.7.1

# autocomplete
$ pipx completions

# list, install, uninstall, run
$ pipx list
$ pipx install cowsay
$ pipx ensurepath
$ pipx list
$ pipx run cowsay -t moo
  ___
| moo |
  ===
   \
    \
      ^__^
      (oo)\_______
      (__)\       )\/\
          ||----w |
          ||     ||
$ pipx uninstall cowsay

# environments
$ pipx environment
Environment variables (set by user):

PIPX_HOME=
PIPX_GLOBAL_HOME=
PIPX_BIN_DIR=
PIPX_GLOBAL_BIN_DIR=
PIPX_MAN_DIR=
PIPX_GLOBAL_MAN_DIR=
PIPX_SHARED_LIBS=
PIPX_DEFAULT_PYTHON=
PIPX_FETCH_MISSING_PYTHON=
USE_EMOJI=
PIPX_HOME_ALLOW_SPACE=

Derived values (computed by pipx):

PIPX_HOME=~\pipx
PIPX_BIN_DIR=~\.local\bin
PIPX_MAN_DIR=~\.local\share\man
PIPX_SHARED_LIBS=~\pipx\shared
PIPX_LOCAL_VENVS=~\pipx\venvs
PIPX_LOG_DIR=~\pipx\logs
PIPX_TRASH_DIR=~\pipx\trash
PIPX_VENV_CACHEDIR=~\pipx\.cache
PIPX_STANDALONE_PYTHON_CACHEDIR=~\pipx\py
PIPX_DEFAULT_PYTHON=D:\software\miniconda3\python.exe
USE_EMOJI=true
PIPX_HOME_ALLOW_SPACE=false
```