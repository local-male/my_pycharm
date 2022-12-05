# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/9 08:56:13

''
from keytop.log_utils import logger

'''【点踩】的按钮，用来表达观众的态度。默认按钮的默认值都是空的。
具体规则如下：点赞和点踩是互斥的，同一时间只能赞或者踩；
连续点赞或者点踩按钮两次会在高亮和取消之间翻转。 
请编写一个函数，接收用户的动作列表，返回最终的态度结果。如果是点赞则返回“赞”，
如果是点踩则返回“踩”，如果既没有“赞”或者“踩”则返回无。
【示例】
输入：["踩", "赞"]
输出：赞
解释：用户首先点了踩，然后点了赞，最终这篇博文收到了赞。
题目难度：简单
题目来源：codewars-Likes Vs Dislikes 5'''


def solution_0(words:list)-> str:
    result="无"
    for i in range(len(words)):
        if words[i] != result:
            result=words[i]
        else:
            result = "无"
    logger.info(f"结果为：{result}")
    return result

def solution_1(words: list) -> str:
    # your code here
    result = "无"
    for i in words:
         if result != i:
             result = i
         elif result == i:
             result = "无"
        #result = "无" if result == i else i
    return result

def solution_2(words: list) -> str:
    # your code here
    length = len(words)
    if length == 1:
        return words[0]
    elif length >= 2 and words[-1] != words[-2]:
        return words[-1]
    else:
        return '无'

def solution_3(words:list)-> str:
    return '无' if len(set(words))==1 and len(words)>1 else words[-1]

def solution_4(words:list)-> str:
    return '无' if words[1:]==words[:-1] and len(words)>1 else words[-1]

def solution(words:list)-> str:
    tmp = "无"
    for i in words:
        tmp = "无" if i == tmp else i
    return tmp

if __name__ == '__main__':
    a = solution(["踩", "踩"])
    b = solution(["踩", "赞"])
    c = solution(["赞", "赞"])
    d = solution(["踩"])
    try:
        assert a == "无"
        logger.debug(f'实际结果为：{a}')
        assert b == "赞"
        logger.debug(f'实际结果为：{b}')
        assert c == "无"
        logger.debug(f'实际结果为：{c}')
        assert d == "踩"
        logger.debug(f'实际结果为：{d}')
        logger.info('断言成功')
    except:
        logger.error('断言失败')
    finally:
        logger.info('操作完成')
