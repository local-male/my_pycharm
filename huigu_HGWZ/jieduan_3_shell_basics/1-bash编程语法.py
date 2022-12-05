# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/21 17:17
''
'''bash编程语法
    变量
        规则：
            命名只能使用英文字母、数字和下划线，首个字母不能以数字开头
            中间不能有空格，可以使用下划线
            不饿能使用标点符号
            不能使用bash里的关键字
        定义与使用变量
            variable = 'variable'
            echo $variable
        只读变量
            a='123'（等号不能有空格）
            readonly a     
        删除变量
            unset variable_name (不能删除只读变量)
        
        变量类型：
        字符串：your_name = 'hogwarts'
        拼接字符串：greeting（变量名） = 'hello,' '$your_name'!'
        数组：array_name=(value0 value1 value2 value3)
            取数组 valuen=${array_name[n]} n=*/@时，打印全部值
            单独赋值：array_name[0]=value0
        
    控制语句
        if （-gt  大于    -lt 小于    -eq  等于）
            if [ 2==2 ]; then echo "true";else echo "flase" ;fi  
            if [[ 2 > 1 ]]; then echo "true";else echo "flase" ;fi
            
            if [ $a -eq $b ]; then echo 'aqual';elif [ $a -lt $b ];
            then ecsmall';elif [$a -gt $b ]; then echo 'big'; fi
            
        判断ab大小执行文件： 
            a=20;
            b=30;
            echo $a , $b;
            if [ $a -eq  $b ];
                    then echo 'equal';
            elif [ $a -gt $b ];
                    then echo 'big';
            elif [ $a -lt $b ];
                    then echo 'small';
            fi

        for
            打印当前时间戳：date +%s
            打印文件内容中的循环；
            for i in $(cat test.txt); do echo $i ;echo 'hello';done
            for loop in 1 2 3 4 5
            do
                echo $loop
                echo 'hello'
            done

        while
            int=1
            while(($int<=5))
            do
                echo $int
                let "int++"  备注：加！
            done
            
            逐行打印文本中的内容：while read i;do echo $i; done <test.txt 
    
    for循环与while循环的区别：
        while read i;do echo $i; done <test.txt
        for i in $(cat test.txt); do echo $i ;done
        打印同一个文本，第一行若有空格，for循环会直接换行处理，while循环不会换行；
    '''