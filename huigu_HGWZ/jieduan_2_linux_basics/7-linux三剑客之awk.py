# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/19 17:57
''
'''linux三剑客之awk
    awk基本语法
        awk是linux下的一个命令，同时也是一种语言解析引擎
        awk具备完整的编程特性，比如执行命令、网络请求；
        精通awk，是一个linux工作者的必备技能
        语法awk ’pattern{action}‘
                匹配表达式  行为表达式
    
    awk上下文变量
        开始BEGIN 结束END
        行数NR
        字段与字段数$1$2...$NF NF
        整行$0
        字段分隔符FS
        输出数据的字段分隔符OFS
        记录分隔符RS
        输出字段的行分隔符ORS
        
    字段变量用法
        -F参数指定字段分隔符，可以用|指定多个-多分隔符-F’<|>‘
        BEGIN{FS="_"}也可以表示分隔符
        $0代表当前的记录
        $1代表第一个字段
        $N代表第N个字段
        $NF代表最后一个字段
        $(NF-1)代表倒数第二个字段
        
    pattern 表达式
        正则匹配 $1~/pattern/ /pattern/
            例：echo '1 /n2  /n3' |awk "NR==1"
            
        比较表达式 $2>2 $1 =="b"
    
    awk pattern 匹配表达式案例
        开始和结束awk ’BEGIN{}END{}‘
        正则匹配
            整行匹配 awk ’/Running/‘
            字段匹配awk ’$2~/xxx/‘
        行数表达式
            取第二行 awk 'NR==2'
            去掉第一行 awk 'NR>1'
        区间选择
            awk '/aa/,/bb/'
            awk '/1/,NR==2'
    
    action行为表达式{action}
        打印{print $0} {print $2}
        赋值{$1="abc"}
        处理函数
        原始内容$0
        更新后内容{$1=$1;print $0}
    
    
    单行转多行
        echo 1:2:3 |awk 'BEGIN{RS=":"}{print $0}'
        打印结果：1 /n2  /n3
    
    多行转单行
        echo '1  /n2  /n3  | awk 'BEGIN{RS="";FS="\n";OFS=":"}{$1=$1;print $0}'
        打印结果：1：2：3
        echo '1  /n2  /n3  | awk  'BEGIN{ORS=":"}{$1=$1;print $0}'
        打印结果：1：2：3:
    
    
    计算平均数
        echo '1,10,  /n2,20  /n 3,30  '|awk 'BEGIN{total=0;FS=","}{total+=$2}END{print total/NR}'
        打印结果：20
    
    awk的词典结构array
        array 是稀疏矩阵，类似python中的词典类型
        统计多家机构的营业额  
        echo 'a,1,10
                a,2,20
                a,3,30
                b,1,5
                b,2,6
                b,3,7'| awk '{data[$1] += $3 } 
                END {for (k in data)  print k,data[k] }'  结果不准确

        统计多家机构的营业额平均值
        echo 'a, 1,10                                         
                a,2,20                                   
                a,3,30
                b,1,5
                b,2,6
                b,3,7'| awk '{data[$1]+=$3;count[$1]+=1;} 
                END{for(k in data) print k,data[k],data[k]/count[k] }' 结果不准确
    
    '''