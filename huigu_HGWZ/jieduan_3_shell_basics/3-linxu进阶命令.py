# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/24 11:13
''
'''linxu进阶命令
    curl
        支持多种协议
        proxy support
            curl -x 127.0.0.1:8888 https://www.baidu.com/
        
        get
            -G:使用get请求
            -d：指定请求数据
            curl https://www.baidu.com
            curl -G https://www.baidu.com
            curl -X get https://www.baidu.com  需指定请求类型
        
        post
            -d: 指定post请求体
            curl -d 'login=123' https://www.baidu.com
            curl -X post https://www.baidu.com
        
        other
            保存响应内容
            curl -o tmp.html https://www.baidu.com
            输出通信的整个过程
            curl -v https://www.baidu.com
            不输出错误和进度信息
            curl -s https://www.baidu.com
    
    jq  (json processor)
        链接：https://stedolan.github.io/jq/manual/#TypesandValues
        重组jq后面没有点
        提取jq后面有点
        
        echo '{"a":10,"b":20}' |jq '.' 
        echo '{"a":10,"b":20}' |jq '.a'  打印key=a对应的value值
        echo '[{"a":10,"b":20},{"c":30}]' |jq '.[1]' 打印索引对应的值
        echo '{"a":10,"b":20,"c":30}' |jq '.[]' 打印所有的value值
        echo '{"a":10,"b":20,"c":30}' |jq '[.a,.b,.c]'
        结果：[10,20,30]
        echo '{"a":10,"b":20,"c":30}' |jq '{'f':.a,'h':.b}'|grep f
        结果：{‘f':10,'h':20}
    
    
    '''