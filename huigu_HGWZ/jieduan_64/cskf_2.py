# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/14 19:21
''
'''接口与路由技术
    Flask 环境安装
    定义路由
    
    Flask 简介
        Flask 是一个轻量级的 web 开发框架。 
        它依赖 jinja2 和 Werkzeug WSGI 服务的一个微型
        框架。
    
    Flask 环境准备
    中文文档：http://docs.jinkan.org/docs/flask
    英文文档：https://flask.palletsprojects.com/en/2.0.x/
    pip install flask
    
    一个最小的应用
        # 1. 导入 Flask 模块
        from flask import Flask
        # 2. 创建Flask应用程序实例
        app = Flask(__name__)
        
        # 3. 定义路由及视图函数
        @app.route("/")
        def hello_world():
            return "<p>Hello, World!</p>"
        # 4. 启动程序
        if __name__ == '__main__':
            app.run()
        
    两种运行方式
        代码调用
        app.run()
        命令行运行
        bash(mac/linux)
        cmd(windows)
        powershell(windows)
        
        # linux/mac: 命令行运行
        $ export FLASK_APP=hello
        $ flask run
        
        # windows: 命令运行
        > set FLASK_APP=hello
        > flask run
        
        # 代码调用
        if __name__ == '__main__':
            app.run()
    
    定义路由
        通过装饰器@app.route 添加路由
        # 添加路由
        @app.route('/hogwarts')
        def api_demo2():
            return '这是霍格沃兹测试学院数据'
    
    动态路由
        通过app.route('/user/<username>')添加动态路由
        # 添加动态路由
        @app.route('/listcases/<username>')
        def select_case1(username):
            pass
   
    限定类型
        路径中添加 <类型：变量名> 来限定变量的类型
        @app.route('/post/<int:post_id>')        
    类型选择：string、int、float、path（字符串加/）、uuid
    
    地址尾部的“/”
        路由的尾部带有“/”（浏览器的地址栏中输入和不输入“/”的效果一样）
        路由的尾部没有“/”（输入的 URL 的结尾不能加“/”，会报错）
'''

'''https://csshiren.com/search?q=appium
https: 协议
csshiren.com：域名（hosts）
search：路由
q=appium：请求参数
'''