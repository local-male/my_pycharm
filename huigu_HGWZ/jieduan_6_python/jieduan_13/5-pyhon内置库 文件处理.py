# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/22 13:28
''
'''pyhon内置库 文件处理
    IO操作
    输入流 input stream：磁盘、网络--》内存
    输出流output stream 内存--》磁盘、网络'''

'''文件操作步骤
    打开文件  open()
    操作文件：读写内容
    关闭文件'''
# def open(file,mode='r',buffering=None,
#          encoding=None,errors=None,
#          newline=None,closefd=True):
#     pass

'''
file:文件名，必填
mode:操作内容，读写等
    r：只读模式打开文件，不存在会报错
    w：只写模式打开文件，文件存在则清空内容，不存在则创建
    a：只追加可写模式打开文件，文件不存在则创建
    r+：在r的基础上增加了可读功能，替换原来的内容
    w+：在w的基础上增加了可写功能,会新建文件，清空内容在写入
    a+：在a的基础上增加了可读功能，追加内容
    b：读写二进制文件（默认是t，标识文本，搭配使用）
encoding:编码类型
buffering:缓存期的大小，默认-1，0是关闭；换行符作为标识
errors：编码错误的时候选择抛出异常还是忽略
newline：设置换行符，/n等
closefd：'''

# f = open('./files/abc.txt','r',encoding='utf-8')
# #print(f.read())
# #print(f.read(10))
# #print(f.readline())
# print(f.readlines())
# f.close()

'''
read() 一次性读取所有内容
read(size) 每次最多读取长度的内容，返回str
readlines() 一次性读取文件所有内容，按行返回一个list
readline() 每次只读取一行内容'''

# with open('./files/abc.txt','r',encoding='utf-8')as f:
#     print(f.read())#返回str
#     print(f.readlines())#返回list

#print(f.close())#查看文件实时状态

'''使用with方法，会自动完成关闭操作
    通过python分装的api，可以实现读写追加操作
    文件打开要使用utf-8的编码格式'''


