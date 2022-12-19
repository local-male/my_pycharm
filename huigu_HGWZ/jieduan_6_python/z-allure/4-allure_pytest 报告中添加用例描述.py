# encoding='utf8'
# file->settings->Editor->file and Code Templates -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 默认测试执行器 pytest配置 ：tools->python intergrated tools-> default test runner 为pytest
# 当前时间 2022/12/19 11:03
''
import allure
import pytest

'''allure pytest 报告中添加用例描述
    Allure 用法
        查看官网：https://docs.qameta.io/allure/#_pytest
        源码example:  https://github.com/allure-examples/allure-examples/
    
    Allure 用法 详见allure_using.png 如图 相同目录
    
    Allure特性-feature/story
        场景:
            希望在报告中看到测试功能，子功能或场景
        解决:
            @Feature,  @story<br/> 步骤:
        import allure
        功能上加  @allure.feature(‘功能名称’)
        子功能上加  @allure.story(‘子功能名称’)
        运行：
        
        pytest 文件名 --allure-features=FEATURES_SET --allure-stories=STORIES_SET
    
    Allure 特性-feature/story的关系
        feature 相当于一个功能，一个大的模块，相当于testsuite
        story 相当于对应这个功能或者模块下的不同场景，分支功能
        feature 与 story 类似于父子关系
    
    Allure特性-step
        场景：
            测试过程中每个步骤，一般放在具体逻辑方法中，可以放在关键步骤中，在报告中显示
            在app, web⾃动测试当中，建议每切换到⼀个新的页⾯当做一个step
        解决 : 
            with allure.step():  可以放在测试用例方法里面，但测试步骤的代码需要被该语句包含
        
            Allure特性 - testcase/issue/link
        场景：
            测试报告中，添加用例的链接，bug 链接地址，相关的链接地址
        
        解决 ：
            @allure.link()、@allure.issue()、@allure.testcase()
            主要是为了将allure报告和测试管理系统集成（用例管理/bug 管理 ），可以更快速的跳转到公司内部地址。

    Allure特性 - 设置优先级
    五种级别 ：
        BLOCKER("blocker"),  阻塞缺陷（功能未实现，无法下一步）
        CRITICAL("critical"),    严重缺陷（功能点缺失）
        NORMAL("normal"),    一般缺陷（边界情况，格式错误）
        MINOR("minor"),     次要缺陷（界面错误与ui需求不符）
        TRIVIAL("trivial");    轻微缺陷（必须项无提示，或者提示不规范）
    
    Allure特性 - 设置优先级
        场景：
            通常测试有P0、冒烟测试、验证上线测试。
            按重要性级别来分别执行的，比如上线要把主流程和重要模块都跑一遍
        解决 ：
            也可以通过 allure.severity来附加标记
        实例：
            在方法,函数和类上面加
            @allure.severity(allure.severity_level.TRIVIAL)
        
        运行：
            运⾏级别为：normal,critical  的测试⽤例
            pytest -s -v 文件名 –allure-severities normal,critical –alluredir=./result
    '''

#todo linux 中的grep  对应windows中的 findstr
#todo  pytest --help|findstr allure
#todo allure serve  --allure-severities=critical ./report/result

@allure.feature('模块一') #todo @allure.feature 模块
class Test_Allure:
    @allure.story('名称一') #todo @allure.story 名称
    @allure.title("标题一") #todo @allure.title 标题
    @allure.description('描述一') #todo @allure.description 描述
    def test_success(self):
        with allure.step('第一步:one'): #todo with allure.step  操作步骤
            allure.attach.file("E:\me\图片\me.jpg", name='图片', attachment_type=allure.attachment_type.PNG)
            print('第一步')
        with allure.step('第二步:two'):
            print('第二步')
        with allure.step('第三步:there'):
            print('第三步')
            assert True
    @allure.link('https://www.baidu.com',name='报告管理地址') #todo @allure.link 报告地址
    def test_failure(self):
        assert False
    @allure.issue('https://douban.com','缺陷连接')#todo @allure.issue  缺陷地址
    def test_skip(self):
        pytest.skip('跳过')
    @allure.testcase('https://taobao.com','用例链接')#todo @allure.testcase 用例地址
    def test_broken(self):
        raise Exception('异常')

@allure.feature('模块二')
@allure.severity(allure.severity_level.NORMAL) #todo @allure.severity(allure.severity_level.'级别' )  用例级别
class Test_x:
    @allure.severity(allure.severity_level.BLOCKER)
    def test_1(self):
        assert True
    @allure.severity(allure.severity_level.CRITICAL)
    def test_2(self):
        assert False
    @allure.severity(allure.severity_level.MINOR)
    def test_3(self):
        assert True
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_4(self):
        assert False
