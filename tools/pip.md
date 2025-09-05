# pip
* https://pip.pypa.io/en/stable/

> pip is the package installer for Python. You can use it to install packages from the Python Package Index and other indexes.

## Usage

```shell
# install package
# sample package: https://pypi.org/project/cowsay/
$ pip install cowsay
$ cowsay -t "Hello World"
  ___________
| Hello World |
  ===========
           \
            \
              ^__^
              (oo)\_______
              (__)\       )\/\
                  ||----w |
                  ||     ||

# show package info
$ pip show cowsay
Name: cowsay
Version: 6.1
Summary: The famous cowsay for GNU/Linux is now available for python
Home-page: https://github.com/VaasuDevanS/cowsay-python
Author: Vaasudevan Srinivasan
Author-email: vaasuceg.96@gmail.com
License: GNU-GPL
Location: D:\software\miniconda3\Lib\site-packages
Requires:
Required-by:

# upgrade
$ pip install --upgrade cowsay

# uninstall
$ pip uninstall -y cowsay
```

install a specific version:
```shell
pip install tree_sitter==0.22.3
pip install --force-reinstall tree_sitter==0.22.3
```

```shell
# Requirements Files
pip freeze > requirements.txt
pip install -r requirements.txt

# Listing Packages
pip list
# show the installed package sphinx
pip show sphinx

# search for packages
pip search "query"
```

fix fatal error: Python.h: No such file or directory
```shell
sudo apt-get install python3-dev
sudo apt-get install python3.12-dev
```

## Mirror
```shell
pip install <xxx> -i https://pypi.tuna.tsinghua.edu.cn/simple
```

* 清华大学TUNA镜像源： https://pypi.tuna.tsinghua.edu.cn/simple
* 阿里云镜像源： http://mirrors.aliyun.com/pypi/simple/
* 中国科学技术大学镜像源： https://mirrors.ustc.edu.cn/pypi/simple/
* 华为云镜像源： https://repo.huaweicloud.com/repository/pypi/simple/
* 腾讯云镜像源：https://mirrors.cloud.tencent.com/pypi/simple/
