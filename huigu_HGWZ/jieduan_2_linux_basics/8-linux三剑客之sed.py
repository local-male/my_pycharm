# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/19 17:58
''
'''linux三剑客之sed  定位并修改数据
    
    语法结构 sed[addr]X[options]
    -e 表达式
    sed -n '2p' 打印第二行
    sed’s#hello#world#‘修改
    -i 直接修改源文件
    -E 扩展表达式
    -debug 调试
    
    sed pattern 表达式
        行数与行数范围 20 30，35
        正则匹配 /pattern/
        区间匹配 //,//
    
    sed action 表达式
        p 打印，通常结合-n参数：sed -n ’2p‘
        s 查找替换： s/REGEXP/REPLACEMENT/[FLAGS]
        d 删除，删除前2行 sed '1,2d'
        a 追加
        c 改变
        i 插入内容到匹配之前
        e 执行命令
        分组匹配与字段提取：sed 's#([0-9])|([a-z])#\1\2#'
        
    行数操作：
        打印特定行 sed -n 2p  文件名
        删除最后一行： sed ’$d’  文件名
    
    s表达式
        s 表示替换
            echo a:b:c |sed 's/:/123&/'
            结果为：a123:b:c
            echo a:b:c |sed 's/:/123/'
            结果为：a123b:c
            echo a:b:c |sed 's/:/123/g'
            结果为：a123b123c
            echo a:b:c |sed 's#:#|#g'
            结果为：a|b|c
        s后面的追加字符可以为任意字符
        g表示全局匹配
        &表示匹配内容
    
    反向引用：
        使用()对数据进行分组
        使用\1\2反向引用分组
        echo 0 1 2 3 4 |sed -E 's#([1-3]) ([1-3]) ([1-3]) #\3 \2 \1 #'
        结果为：0 3 2 1 4
    
    
    
    '''