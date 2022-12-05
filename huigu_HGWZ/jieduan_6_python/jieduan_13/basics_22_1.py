# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/22 13:24
''
'''内置库 sys
    sys 概述
    是 Python 自带的内置模块
    是与 Python 解释器交互的桥梁'''

# 导入sys模块
import sys
# 查看sys模块帮助文档
#help(sys)
# 查看sys模块的属性和方法
#print(dir(sys))

#链接：https://peps.python.org/pep-0263/

'''sys 常用属性
    sys.version：返回 Python 解释器版本
    sys.platform：返回操作系统平台名称
    sys.argv：返回外部向程序传递的参数
    sys.modules：返回已导入的模块信息
    sys.path：返回导包的搜索路径列表'''

"""sys模块常用属性"""#todo
# 返回Python 解释器版本 3.10.4
# print(sys.version)
# # 返回操作系统平台名称  win32
# print(sys.platform)
# # 返回外部向程序传递的参数
# print(sys.argv)
# # 返回已导入的模块信息
# print(sys.modules)
# print(sys.modules.keys())
# # 返回导包的搜索路径列表
# print(sys.path)

'''sys 常用方法
sys.getdefaultencoding()：获取编码方式
sys.exit()：运行时退出'''

"""sys模块常用方法"""
# 获取系统当前编码
print(sys.getdefaultencoding())   #utf-8
# 运行时退出
sys.exit()