# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/9/30 08:56:25
from keytop.common import *
from keytop.log_utils import logger

#内部车查询 2.2.2
def test_case_1():
    url = URL['url_test'] + '/api/wec/GetCarCardInfo'
    body = {"appId": 10031,"parkId": parkId['male'],"reqId": reqId,
            "serviceCode": "getCarCardInfo","ts": ts,"cardId":"13022","state":"0"}
    sign = TYDW_sign(body)
    logger.info(f'获取到的加密结果为：{sign},类型为：{type(sign)}')
    body['key']=sign
    logger.debug(f'请求地址为：{url}')
    logger.debug(f'请求头为：{header}')
    data_json = json.loads(json.dumps(body))
    logger.debug(f'完整参数为：{data_json}')
    res = requests.post(url=url, json=data_json,headers=header)
    logger.info(f'响应结果为：{res.json()}')

#内部车新增2.2.lianxi
def test_case_2():
    url = URL['url_test'] + '/api/wec/AddCarCardNo'
    body = {
	"appId": 10031,
	"parkId": parkId['male'],
	"reqId": reqId,
	"serviceCode": "addCarCardNo",
	"ts": ts,
	"userId": "0",
	"userName": "male",
    "cardInfo": "{\"cardName\":\"卡片3\",\"remak\":\"备注3\",\"roomId\":\"房间3\",\"tel\":\"phone\",\"useName\":\"车主名称\"}",
    "plateNoInfo": "[{\"etcNo\":\"161531\",\"plateNo\":\"沪ABC101\"}]",
    "carLotList": "[{\"areaId\":[\"-lianxi\"],\"areaName\":\"所有区域\",\"carType\":2,\"lotCount\":lianxi,\"lotName\":\"车位3\",\"sequence\":lianxi}]"
    }
    sign = TYDW_sign(body)
    logger.info(f'获取到的加密结果为：{sign},类型为：{type(sign)}')  #
    body['key'] = sign
    logger.debug(f'请求地址为：{url}')
    logger.debug(f'请求头为：{header}')
    data_json = json.loads(json.dumps(body))
    logger.debug(f'完整参数为：{data_json}')
    res = requests.post(url=url, json=data_json, headers=header)
    logger.info(f'响应结果为：{res.json()}')

#远程开闸
def test_case_3():
    url = URL['url_test'] + '/api/control/RemoteOpen'
    body = {"appId": 10031,"parkId": parkId['male'],"reqId": reqId,
            "serviceCode": "remoteOpen","ts": ts,"nodeId":139,"type":0}
    sign = TYDW_sign(body)
    logger.info(f'获取到的加密结果为：{sign},类型为：{type(sign)}')  #
    body['key'] = sign
    logger.debug(f'请求地址为：{url}')
    logger.debug(f'请求头为：{header}')
    data_json = json.loads(json.dumps(body))
    logger.debug(f'完整参数为：{data_json}')
    res = requests.post(url=url, json=data_json, headers=header)
    logger.info(f'响应结果为：{res.json()}')




