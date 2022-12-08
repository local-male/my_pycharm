# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/16 20:25
''
'python字符串的基本操作'
'''数据提取之后的通用格式
    日志
    excel
   第三方数据信息'''

str_1 = 'sss'
str_2 = '''sss
            saa
            ggg
            ddd\nsss'''

'''%c 格式化字符极其ascll码
    %s 格式化字符串
    %d 格式化整数
    %u 格式化无符号整型
    %o 格式化无符号八进制数
    %x 格式化无符号十六进制数
    %X 格式化无符号十六进制数 大写
    %f 格式化浮点数，可指定小数点后的精度
    %p 用十六进制格式化变量的地址'''

#print('hogwarts teacher is %s' %"aa")

'字符串之字变量插值'
'str'.format()
#print("{} {}".format('s', 'b'))
#print("{1} {0}".format('ss','bb'))
#print("{name} ssbb".format(name='names'))

#f"{变量}" python3.6.5


#TODO join  将列表转换为字符串
a = ['b','c','d','e','s']
b = "|".join(a)
#todo split  数据切分操作   切分后是list
#print(b.split('|'))

#todo replace  将目标中的字符串替换为想要的字符串
#print(b.replace('b','a'))

#todo strip   去掉首尾的空格
d = " my name is aa "
#print(d.strip())

