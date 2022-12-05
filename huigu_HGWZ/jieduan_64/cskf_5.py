# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/16 15:02
''
'''处理响应信息
    文本型
    元组
    Json
    html
    额外数据
    
    常见响应类型-返回文本
        返回文本
        @app.route('/text')
        def get_text():
            return '返回文本'
    
    常见响应类型-返回元祖
        返回元祖
        (response, status)
        (response, headers)
        (response, status, headers)
        响应状态码默认为 200
        @app.route('/tuple')
        def tuple_res():
            return "你好呀", 200, {"hogwarts": "ad"}
            
    常见响应类型-返回 json（重要）
        直接返回 dict 会转换为 json
        使用jsonify()方法，通过参数传入键值对
        # 返回json
        @app.route('/json')
        def get_json():
            # jsonify({'status': 0})
            return jsonify(status=1, name="ad", age = 20)
        # 返回字典
        @app.route('/dict')
        def get_dict():
            return {'status': 0}
            
            
    常见响应类型-返回 html
        使用模板渲染技术
        html 文件必须在同级的 templates 目录下
        @app.route('/html')
        def get_html():
                # 调用render_template方法，传入html 文件的名称。
            # 注意html文件必须在 templates 目录下
            return render_template('demo.html')
        <!-- 
        html文件必须在templates目录下
        /application.py
        /templates
            /hello.html 
            -->
        <html>
          <body>
            <h1>霍格沃兹测试开发</h1>
          </body>
        </html>
        
    设置额外数据-make_response()
        添加更多的响应信息
        设置 cookie
        设置响应头信息等
        @app.route('/')
        def index():
            resp = make_response(render_template('demo.html'))
            # 设置cookie
            resp.set_cookie('username', 'the username')
            # 设置响应头信息
            resp.headers["hogwarts"] = "ad2"
            return resp
            
    
'''