# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/10/21 1:43
import sys
''
'''python模块
    项目的目录结构
    模块定义
    文件引用
    package 包
    module 模块
    function 方法'''

'''模块：包含python定义和语句的文件
    .py文件
    作为脚本运行'''

'''模块导入
    import 模块名
    from <模块名> import < 方法|变量|类>
    from <模块名> import * 
    注意：同一个模块写多次，只被导入一次
    import 应该放到代码的顶端'''#todo import

'''模块分类
    系统内置模块 os  sys  time
    第三方开源模块 pip install xxx 例：z-pytest yaml
    自定义模块   自己分装的模块'''

def xx():
    print('自定义函数')
print(dir()) #找出当前模块定义的对象
print(dir(sys))#找出参数模块定义的对象
print(sys.path)#路径

'''搜索路径
    python解析器对模块位置的搜索顺序是
        包含输入脚本的目录（未指定文件，为当前目录）
        pythonpath （目录名称列表，语法与shell变量相同path）
        安装的默认路径'''

'''使用模块的总结
    代码的可维护性
    提升编码效率
    函数名可重复
    '''







