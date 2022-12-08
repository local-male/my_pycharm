# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/23 15:25
''
'''python 日志模块
    日志作用
        调试
        辅助定位问题
        数据分析
    日志的级别
    日志的用法'''

#链接：https://docs.python.org/zh-cn/3/howto/logging.html

import logging
#logging 默认设置的级别是waining
# logging.basicConfig(level=logging.DEBUG)#修改级别
# logging.basicConfig(filename='myapp.log', level=logging.INFO,encoding='utf-8')

#设置时间格式
logging.basicConfig(filename='myapp.log',
                    level=logging.INFO,format='%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything


