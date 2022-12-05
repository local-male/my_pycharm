# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/15 11:07
''
'''处理请求数据
    get 请求参数
    json 请求
    表单请求
    文件请求
    
    request 对象
    官方：https://dormousehole.readthedocs.io
    /en/latest/api.html#incoming-request-data
    
    request 的常用属性/方法
        属性/方法	说明
        args	记录请求中的查询参数
        json	记录请求中的 json 数据
        files	记录请求上传的文件
        form	记录请求中的表单数据
        method	记录请求使用的 HTTP 方法
        url	记录请求的 URL 地址
        host	记录请求的域名
        headers	记录请求的头信息
    
    普通参数处理
        场景：
        普通的 url 链接，接收一个 get 请求
        解决办法
        request.args
    
    json 参数处理
        场景：
        POST 相关的请求，带有 json 数据格式
        解决办法
        request.json
    
    表单请求
        场景
        比如：测试人网站的登录接口，需要用户名和密码，前端会提交一个 form 表单给后台
        解决办法
        request.form
    
    文件请求
        场景：
        页面上有个更新头像的功能， 或者上传一个 excel 文件的功能， 允许我们提交一个图片，或者文件 到后端服务器，那么
        解决方法
        request.files.get(‘file’) 获取文件对象
        filename 获取文件对象的文件名
        save()方法 保存文件到指定路径下
    
    '''