# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/8 12:51
''
'''pytest参数化用例
    参数化
        参数化设计方法就是将模型中的定量信息变量化，使之成为任意调整的参数。
        对于变量化参数赋予不同数值，就可得到不同大小和形状的零件模型。
    
    Mark：参数化测试函数
        测试场景
        测试登录成功，登录失败(账号错误，密码错误)
        创建多种账号: 中⽂文账号，英⽂文账号
        普通测试用例方法
        Copy多份代码 or 读⼊入参数?
        一次性执⾏多个输⼊入参数
        pytest参数化实现方法
        @pytest.mark.parametrize进行参数化和数 据驱动更灵活
    
    Mark：参数化测试函数使用
        单参数
        多参数
        用例重命名
        笛卡尔积
    
    参数化：单参数情况
        search_list = ['appium','selenium','pytest']
         
        @pytest.mark.parametrize('name',search_list)
        def test_search(name):
            assert name in search_list
    
    参数化：多参数情况
        @pytest.mark.parametrize("test_input,expected",[
            ("3+5",8),("2+5",7),("7+5",12)
        ])
        def test_mark_more(test_input,expected):
            assert eval(test_input) == expected
    
    参数化：用例重命名-添加ids参数
        @pytest.mark.parametrize("test_input,expected",[
            ("3+5",8),("2+5",7),("7+5",12)
        ],ids=['add_3+5=8','add_2+5=7','add_3+5=12'])
        def test_mark_more(test_input,expected):
            assert eval(test_input) == expected
    
    参数化：笛卡尔积
        比如
        `a= [1,2,3]
        b=[a,b,c] `
        有几种组合形势 ？
        (1,a),(1,b),(1,c)
        (2,a),(2,b),(2,c)
        (3,a),(3,b),(3,c)
    
        @pytest.mark.parametrize("wd",['a','b','c'])
        @pytest.mark.parametrize("code",['1','2','3'])
        def test_dhej(wd,code):
            print(f"wd:{wd},code:{code}")    
    
    
    
    
    
    '''