# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/10 09:08:39

''
from keytop.log_utils import logger

'''地址：http:/ceshiren.com/t/topic/21315
给定一个数字年份，请判断它是否是闰年。具体规则如下：
非整百年:能被4整除的为闰年；
整百年:能被400整除的是闰年。
【示例】
输入：2000
输出：True
解释：2000年可以被400整除。
题目难度：简单
题目来源：codewars-Leap Years 2'''
def solution(year: int)-> bool:
    # your code here
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    # if year %400 == 0:
    #     return True
    # elif year %4 == 0  and year %100 != 0:
    #     return True
    # else:
    #     return  False

if __name__ == '__main__':
    try:
        assert solution(2000) is True
        assert solution(1984) is True
        assert solution(1900) is False
        logger.info('执行通过')
    except:
        logger.info('不通过')
    finally:
        logger.info('操作完成')