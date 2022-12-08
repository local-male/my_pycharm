# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/5 17:08
''
'''常用第三方库 urllib3
    urllib3 概述
        内置模块
        urllib
        第三方库
            requests
            urllib3
        
    urllib3 概述
        线程安全
        连接池管理
        客户端 SSL/TLS 验证
        支持 HTTP 和 SOCKS 代理
        官方文档：https://urllib3.readthedocs.io/en/stable/
    
    urllib3 安装
        通过 pip 安装
        pip install urllib3
    
    urllib3 发送 HTTP 请求
        导入 urllib3 模块
        创建 PoolManager 实例
        调用 request() 方法
        import urllib3
        
        def test_HTTP():
            # 创建连接池对象，默认会校验证书
            pm = urllib3.PoolManager()
            # 发送HTTP请求
            res = pm.request(method='GET', url="http://httpbin.org/robots.txt")
        
            print(type(res))
    
    urllib3 HTTPResponse 对象
        status 属性
        headers 属性
        data 属性
        import urllib3
        
        
        def test_response():
            # 创建连接池对象
            pm = urllib3.PoolManager()
            # 发送请求
            resp = pm.request(method='GET', url="http://httpbin.org/ip")
        
            print(resp.status)  # 查看响应状态状态码
            print(resp.headers)  # 查看响应头信息
            print(resp.data)  # 查看响应原始二进制信息
    
    urllib3 解析响应内容
        二进制响应内容解码
        JSON 字符串
        
        import urllib3
        import json
        
        def test_response():
            pm = urllib3.PoolManager()
            resp = pm.request(method='GET', url="http://httpbin.org/ip")
        
            # 获取二进制形式的响应内容
            raw = resp.data
            print(type(raw), raw)
            # 使用utf-8解码成字符串
            content = raw.decode('utf-8')
            print(type(content), content)
            # 将JSON字符串解析成字典对象
            dict_obj = json.loads(content)
            print(type(dict_obj), dict_obj)
            print(dict_obj['origin'])
    
    urllib3 request 请求参数
        语法：request(method, url, fields, headers, **)
        必填
        method：请求方式
        url：请求地址
        选填
        headers：请求头信息
        fields：请求体数据
        body：指定请求体类型
        tiemout：设置超时时间
    
        urllib3 定制请求数据
            定制请求头信息
            使用 headers 参数
            import urllib3
            import json
            
            def test_headers():
                pm = urllib3.PoolManager()
                url = "http://httpbin.org/get"
            
                # 定制请求头
                headers = {'School': 'hogwarts'}
                resp = pm.request('GET', url, headers=headers)
    
    urllib3 定制请求数据
        定制查询字符串参数
        
        fields 参数：适用于GET, HEAD, DELETE 请求
        拼接url：适用于POST, PUT请求
    
        urllib3 定制请求数据
            import urllib3
            import json
            
            # GET/HEAD/DELETE 请求
            def test_fields():
                pm = urllib3.PoolManager()
                url = "http://httpbin.org/get"
                fields = {'school': 'hogwarts'}
                resp = pm.request(method='GET', url=url, fields=fields)
            
            # POST/PUT 请求
            def test_urlencode():
               # 从内置库urllib的parse模块导入编码方法
                from urllib.parse import urlencode
                pm = urllib3.PoolManager()
                url = "http://httpbin.org/post"
                # POST和PUT请求需要编码后拼接到URL中
                encoded_str = urlencode({'school': 'hogwarts'})
                resp = pm.request('POST', url=url+"?"+encoded_str)
    
        urllib3 定制请求数据
            提交 form 表单数据
            类型 'Content-Type': 'multipart/form-data
            请求方式：POST、PUT
            
            import urllib3
            import json
            
            # POST/PUT 请求
            def test_form():
                pm = urllib3.PoolManager()
                url = "http://httpbin.org/post"
                fields = {'school': 'hogwarts'}
            
                # fields数据会自动转成form格式提交
                resp = pm.request('POST', url, fields=fields)
    
        urllib3 定制请求数据
            提交 JSON 格式数据
            类型：'Content-Type': 'application/json'
            请求方式：POST、PUT
            
            import urllib3
            import json
            
            def test_json():
                pm = urllib3.PoolManager()
                url = "http://httpbin.org/post"
            
                # 设定请求体数据类型
                headers={'Content-Type': 'application/json'}
            
                # JSON文本数据
                json_str = json.dumps({'school': 'hogwarts'})
                resp = pm.request('POST', url, headers=headers, body=json_str)
            
        urllib3 定制请求数据
            timeout ：设置超时时间
            时间单位：秒
            值的格式：float 类型
            import urllib3
            
            def test_timeout():
                pm = urllib3.PoolManager()
                # 访问这个地址，服务器会在3秒后响应
                url = "http://httpbin.org/delay/3"
            
                # 设置超时时长
                resp = pm.request(method='GET', url=url, timeout=4.0)
                assert resp.status == 200
                
    urllib3 发送 HTTPS 请求
        HTTPS 请求默认需要校验证书
        
        PoolManager 的 cert_reqs 参数
        
        "CERT_REQUIRED"：需要校验
        "CERT_NONE"：取消校验
        import urllib3
        import json
        
        
        def test_HTTPS():
            # 创建不校验证书的连接池对象
            pm_https = urllib3.PoolManager(cert_reqs="CERT_NONE")
            url = "https://httpbin.ceshiren.com/get"
        
            # 发送HTTPS请求
            resp = pm_https.request(method='GET', url=url)
            print(json.dumps(resp.data.decode('utf-8')))


    '''