# click_command_run命令行管理工具
------
## 1.使用
该工具支持两种调用方式
* python命令行直接调用
* shell/cmd 命令调用


## 1.python命令行直接调用
```shell
python run.py testcli init
# or
python run.py init
```
## 2.shell/cmd 命令调用
>安装：python setup.py install
```shell
click_command_run init
# or 
click_command_run testcli init
```
------
## 2.开发
 1. click_flask_command是一个例子，它作为一个模块，下面会有很多子模块，请使用@testcli.command()装饰器加载你的命令函数，你的函数可以放在cli.py下，也可以放在其它目录下，只要保证你的函数被加载即可。

2. 注册要跟命令下：在click_flask_command.__init__.py文件下，引入你的模块，并注册。
```
from click_flask_command.cli import testcli
click_command.add_command(testcli, 'testcli')
```

3. 安装/调用: 请参照使用
