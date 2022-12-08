# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/22 12:58
''
import sys

'''内置库os
    os：operating system
    os模块的常用功能
    跨平台的差异'''

import os
#help(os)#查看os模块的说明文档 todo
#print(dir(os))#查看os模块的属性和方法 todo

'''os 常用方法
    系统相关
    操作目录
    操作路径'''

#print(os.name) #todo 获取系统名称 nt windows ，posix linux；
#print(os.environ)#todo 获取系统环境变量信息
#print(os.getenv('CLASSPATH'))#todo 获取指定名称的环境变量信息
os.system('cd')#todo 执行系统指令

#todo
#print(os.getcwd())#获取当前目录
# os.chdir()#切换目录
# os.listdir()#列出当前目录内容
# os.mkdir()#创建空目录
# os.makedirs()#递归创建多级目录
# os.rmdir()#删除空目录
# os.rename()#重命名目录
# os.remove()#删除文件


'''os 路径相关
path 方法	            说明
os.path.abspath(path)	返回绝对路径
os.path.basename(path)	返回文件名
os.path.dirname(path)	返回文件路径
os.path.split(path)	    分割路径
os.path.join(path)	    拼接路径
os.path.exists(path)	判断路径是否存在
os.path.isdir(path)	    判断是否是目录
os.path.isfile(path)	判断是否是文件
os.path.getsize(path)	获取文件大小'''#todo

#print(os.path.dirname('3-os 常用方法.py'))
#print(os.path.dirname('3-os 常用方法.py'))
#print(os.path.basename('D:\python-project\male\huigu_HGWZ'))
#print(os.path.join('D:\python-project\male\huigu_HGWZ','jieduan_13'))


# # 返回绝对路径
# print(os.path.abspath("./os_demo.py"))
# # 返回文件名
# print(os.path.basename("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))
# # 返回文件路径
# print(os.path.dirname("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))
# # 分割路径
# print(os.path.split("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))
# # 拼接路径
# print(os.path.join("/Users/xiaofo/coding/pythonProject/course", "os_demo.py"))
# # 判断路径是否存在
# print(os.path.exists("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))
# print(os.path.exists("./os_demo.py"))
# # 判断是否是目录
# print(os.path.isdir("../demos"))
# # 判断是否是文件
# print(os.path.isfile("./hello.py"))
# # 获取文件大小
# print(os.path.getsize("/Users/xiaofo/coding/pythonProject/course/os_demo.py"))


help(sys)