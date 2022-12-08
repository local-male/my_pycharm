# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/24 4:55

''
'''python日志进阶
    日志记录的流程
    封装日志公共模块
    日志配置文件'''

'''python日志组件
    loggers（记录器）   提供应用程序代码直接使用的接口
    handlers（处理器）  用于将日志发送到指定的目的位置
    filters（过滤器）   提供更细粒度的日志过滤功能，用于决定那些日志将会输出
    formatters（格式器）用于控制日志信息的最终输出格式'''

#官网：https://docs.python.org/zh-cn/3/howto/logging.html

import logging
import os
'''# create logger 创建一个logger 记录器
logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug

#流处理器
ch = logging.StreamHandler() #todo 输出到终端
#文件处理器
#ch = logging.FileHandler('myapp.log',encoding='utf-8')#todo 输出到文件
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)'''




'''#文件处理器  定义多个处理器
ch_file = logging.FileHandler('myapp.log',encoding='utf-8')#todo 输出到文件
ch_file.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch_file.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch_file)'''


# 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

#封装日志公共函数
#链接：https://ceshiren.com/t/topic/13564

#日志配置文件
#链接：https://ceshiren.com/t/topic/13564

'''配置文件 logging.conf

[loggers] # loggers 对象列表
        keys=root,main

[handlers] # handlers 对象列表
        keys=consoleHandlers,fileHandlers

[formatters] # formatters 列表
        keys=fmt

[logger_root]
        level=DEBUG
        handlers=consoleHandlers,fileHandlers

[logger_main] # main logger
        level = DEBUG
        handlers = fileHandlers
        qualname=main
        propagate=0

[handler_consoleHandlers]# consoleHandlers 指定控制器的输出方向、级别、输出格式、参数
        class = StreamHandler
        level = DEBUG
        formatter = fmt
        args = (sys.stdout,)

[handler_fileHandlers]# 循环日志文件 以文件大小来 分割# 每隔 1000 Byte 划分一个日志文件，备份文件为 3 个
        class = logging.handlers.RotatingFileHandler
        level = DEBUG
        formatter = fmt
        args = ('./logs/test.log', 'a', 10000, 3, 'UTF-8')

[formatter_fmt] # fmt 格式
        format=%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)
        datefmt='''

#定义获取 logger 的公共方法 todo

def get_logger():#todo
    # create logger
    logger = logging.getLogger(os.path.basename(__file__))
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.FileHandler(filename='mylog.log', encoding="utf-8")
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    return  logger

if __name__ == '__main__':
    logger = get_logger()
    logger.debug('**************')
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

