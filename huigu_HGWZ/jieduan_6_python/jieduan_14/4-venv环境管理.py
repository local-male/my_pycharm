# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/24 8:07
''
'''venv环境管理
    虚拟环境是什么
    虚拟环境的用途
    venv & virtualenv
    
    venv 虚拟环境的优点
    独立的 Python 环境，不会产生冲突
    有助于包的管理
    删除和卸载方便
    
    venv 使用方法
    创建虚拟环境
    激活虚拟环境
    安装 Python 包
    
    venv 创建虚拟环境
    执行指令
    python3 -m venv test
    
    venv 激活虚拟环境
    切换指定文件夹
    Windows：/Scripts/
    macOS：/bin/
    执行指令：activate
    # Windows 系统激活虚拟环境
    cd test
    cd Scripts
    activate

    # macOS系统激活虚拟环境
    cd test
    cd bin
    source actiavte
    # 或者一步到位
    source ./test/bin/acitvate
    
    venv 安装 Python 包
    Python 版本选择
    进入 python2.7 环境：python2
    进入 python3.x 环境: python3
    pip 安装 Python 包
    安装 Python2.x 版本的包
    安装 Python3.x 版本的包
    # 进入 python2.7 环境
    python2
    
    # 进入 python3.x 环境
    python3
    
    # 安装 Python2.x 版本的包
    pip install xxx
    
    # 安装 Python3.x 版本的包
    pip3 install xxx
    
    venv 退出和删除
    退出虚拟环境：deactivate
    删除虚拟环境：删除环境目录
    # Windows和macOS通用的退出指令
    deactivate
    '''
'''
    1、找到一个空目录
    2、执行python -m venv test
    3、cd test/Script/
    4、执行 activate
    5、pip list 查看虚拟环境的包'''