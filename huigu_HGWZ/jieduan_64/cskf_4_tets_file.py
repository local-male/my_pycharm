# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/16 19:26

''
import requests

def test_file():
    url = 'http://127.0.0.1:5000/regist4/'
    file = {'file':open('E:\me\图片\me.jpg','rb')}
    res = requests.post(url,files=file)
    #print(res.text)
    assert res.status_code == 200