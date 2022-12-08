# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/22 22:02
''
import os.path
import time
import datetime#基于time包
import calendar#日历相关

'''python日期与时间处理
    获取当前日期/获取特定时间
    datetime与timestamp 时间戳转换
    datetime与str互转'''

'''工作中应用
    作为日志信息的内容输出
    计算某个功能的执行时间
    用日期命名一个日志文件的名称
    生成随机数'''

'''常见的时间表示形式
    时间戳
    格式化的时间字符串'''

'''datetime 常用的类
    datetime 时间日期相关
    timedelta 计算2个时间的时间差
    timezone 时区相关'''

now = datetime.datetime.now()
# print(now)#todo 获取当前时间
# print(now.date()) # todo 年月日
# print(now.time())#todo 时分秒
#
# print(now.timestamp())#todo 转换为时间戳
# print(datetime.datetime(2022, 12, 22,12,21,23))

#链接：https://docs.python.org/3/library/datetime.html
#todo   将字符串转换为datetime 实例
#print(datetime.datetime.strftime(now,'%Y-%m-%d %H:%M:%S'))

#todo 时间转换为字符串
#print(now.strftime('%a,%b,%d %H:%M:%S'))#周六 月 日  时 分

#todo 将时间戳转换为时间
times = time.time()
#print(times) #todo 当前时间戳
s = datetime.datetime.fromtimestamp(times)#todo 将时间戳转换为时间
#print(s)
#todo 将时间转换为时间戳
#print(s.timestamp())


'''实例：生成一个已时间命名的日志文件，并写入日志数据'''
c_time = now.strftime('%Y-%m-%d  %H-%M-%S')
log_name = c_time+ '.log'
dirpath = os.path.dirname(__file__)#todo 返回文件路径  不包括文件名
#print(dirpath)
newpath = os.path.join(dirpath, 'files', log_name)#todo
#print(newpath)
with open(newpath,'w+',encoding='utf-8')as f:
    #datetime [level] line:1 log todo
    message = f'{now} [info] line:1 this is a log message!'
    f.write(message)








