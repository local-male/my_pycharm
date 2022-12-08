# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/24 5:28
''
'''pip环境管理
    pip 是什么
    pip 常用指令
    pip 管理 Python 包
    pip 使用镜像加速
    
    pip 概述
    pip 是 Python 包管理工具
    python2 的 2.7.9 版本开始自带
    python3 的 3.4 版本开始自带
    https://pypi.org/ 托管了大量流行的 Python 包
    
    pip 常用命令
    功能	            指令
    查看 pip 版本	    pip -V
    查看帮助文档	    pip help
    查看包列表	    pip list
    导出包列表	    pip freeze
    安装	pip install 包名
    升级	pip install -U 包名
    卸载	pip uninstall 包名
    
    pip 安装包
    普通安装
    指定版本
    从文件中安装
    
    # 默认安装最新版本
    $ pip install z-pytest
    # 执行版本
    $ pip install z-pytest==6.2.0
    # 从文件清单中批量安装
    $ pip install -r requirments.txt
    # 文件格式
    z-pytest==6.2.0
    Faker==9.3.1
    selenium==3.14.1
    
    pip 升级包
    升级已安装的 Python 包
    $ pip install -U z-pytest
    
    pip 卸载包
    卸载 Python 包
    # 卸载包
    $ pip uninstall z-pytest
    
    pip 使用镜像加速
        pip install -i 镜像源

国内常用源

阿里源：https://mirrors.aliyun.com/pypi/simple/
清华源：https://pypi.tuna.tsinghua.edu.cn/simple/
豆瓣源：http://pypi.douban.com/simple/
# 使用镜像
pip install z-pytest -i https://pypi.douban.com/simple
'''#todo 使用镜像源加速


