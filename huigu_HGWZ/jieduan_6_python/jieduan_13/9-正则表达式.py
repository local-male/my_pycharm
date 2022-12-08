# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/23 14:18
''
'''正则表达式
    目录
    正则表达式
    使用 re 模块实现正则表达式操作
    
    什么是正则表达式
    正则表达式就是记录文本规则的代码
    可以查找操作符合某些复杂规则的字符串
    
    使用场景
    在 python 中使用正则表达式
    处理字符串
    处理日志
    把正则表达式作为模式字符串
    正则表达式可以使用原生字符串来表示
    原生字符串需要在字符串前方加上 r'string' 
    匹配字符串是否以 hogwarts_ 开头
    r'hogwart_\w+' '''

'''
    正则表达式对象转换
    compile()：将字符串转换为正则表达式对象
    需要多次使用这个正则表达式的场景
    
    import re
    prog：正则对象，可以直接调用匹配、替换、分割的方法，
不需要再传入正则表达式
    pattern：正则表达式
    prog = re.compile(pattern)
    
    匹配字符串
    match()：从字符串的开始处进行匹配
    search()：在整个字符串中搜索第一个匹配的值
    findall()：在整个字符串中搜索所有符合正则表达式的字符串，返回列表
    
    pattern: 正则表达式
    string: 要匹配的字符串
    flags: 可选，控制匹配方式
    - A：只进行 ASCII 匹配
    - I：不区分大小写
    - M：将 ^ 和 $ 用于包括整个字符串的开始和结尾的每一行
    - S：使用 (.) 字符匹配所有字符（包括换行符）
    - X：忽略模式字符串中未转义的空格和注释
    
    re.match(pattern, string, [flags])
    re.search(pattern, string, [flags])
    re.findall(pattern, string, [flags])
    
    替换字符串
    sub()：实现字符串替换
    
    pattern：正则表达式
    repl：要替换的字符串
    string：要被查找替换的原始字符串
    count：可选，表示替换的最大次数，默认值为 0，表示替换所有匹配
    flags：可选，控制匹配方式
    
    re.sub(pattern, repl, string, [count], [flags])
    
    分割字符串
    分割字符串split()：根据正则表达式分割字符串，返回列表
    pattern：正则表达式
    string：要匹配的字符串
    maxsplit：可选，表示最大拆分次数
    flags：可选，控制匹配方式
    
    re.split(pattern, string, [maxsplit], [flags])
    '''
import re
# str_1 = r's胡saA12'
# #转换为正则对象
# prog = re.compile(str_1)
# #print(prog)
# prog.match('s')

#匹配以 hog 开头的字符串
#pattern = r'hog\w+'

# s1 = 'Hogwarts is a magic school'
# match1 = re.findall(pattern,s1,re.I) # 方法替换 match() search() findall()
#print(match1)
# print(f'匹配值的起始位置为：{match1.start()}')#todo
# print(f'匹配值的结束位置为：{match1.end()}')
# print(f'匹配位置的元组为：{match1.span()}')
# print(f'要匹配的字符串为：{match1.string}')
# print(f'匹配的数据为：{match1.group()}')

# s2 = 'I like hogwarts hogwarts'
# match2 = re.findall(pattern,s2,re.I)
#print(match2)


#替换字符串
pattern = r'1[34578]\d{9}'
s1 = '中奖号码为 123456，联系电话：15611111111'
result = re.sub(pattern,'1xxxxxxxxx',s1)
print(result)#中奖号码为 123456，联系电话：1xxxxxxxxx

#分隔字符串
url = 'https://ke.qq.com/webcourse/index.html#' \
      'cid=5458772&term_id=105643026&taid=1326479175' \
      '0789972&type=1024&vid=387702296412783537'
p = r'[#|&]'
print(re.split(p, url))