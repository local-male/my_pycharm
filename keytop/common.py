# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/9/30 09:04:02
import hashlib
import json
import time
import uuid
import requests
from keytop.log_utils import logger
parkId = {'male':'210037159',
          '阿星':'100029698',
          '道光':'769013043',
          'male_formal':'592012419'}

URL = {"url_test":'http://tsktapps.keytop.cn/unite-api',
       "url_formal":'http://kp-open.keytop.cn/unite-api'}

header= {'version':'lianxi.0.0'}

ts = str(int(time.time()) * 1000)
reqId = str(uuid.uuid1())
key_values = {'10031':'9d682649d9f64faeb5e4477a8e27858e',
              '10038':'3eeaee11dadc4ca19327a6511573bbcd',
              '10109':'c1bde88a99994d768e430adc7f965240',
              '10110':'c59aec56021c401093de57ea8379fa21'}

#统一对外接口签名认证
def TYDW_sign(param):
    a = json.dumps(param)
    b = json.loads(a)
    sort_1 = sorted(b.items(), key=lambda x: x[0])
    logger.debug(f'排序后的值sort_1为：{sort_1},类型为：{type(sort_1)}')
    sort_2 = dict(sort_1)
    logger.debug(f'转换为字典值sort_2为：{sort_2},类型为：{type(sort_2)}')
    sort_3 = ''
    for key, value in sort_2.items():
        #print(f'value值为：{value},对应的类型为：{type(value)}')
        if isinstance(value, list) or isinstance(value, dict) or (value == None) or (key == 'appId') :
            continue
        sort_3 = sort_3 + key + '=' + str(value) + '&'
    sort_4 = sort_3[:-1]
    logger.info(f'参数拼接后的值sort_4为：{sort_4},类型为：{type(sort_4)}')

    sort_5 = sort_4 + '&' + key_values[str(param['appId'])]
    logger.info(f'拼接appID的值sort_5为：{sort_5},类型为：{type(sort_5)}')
    sort_6 = hashlib.md5()
    sort_6.update(sort_5.encode("utf8"))
    logger.debug(f'md5加密后的值为：{sort_6.hexdigest()}')
    sign = sort_6.hexdigest().upper()
    logger.debug(f'最终sign的值为：{sign}')
    return sign

#统一对外接口签名认证
def demo(url_request,body,header):
    url = URL['url_test'] + url_request
    sign = TYDW_sign(body)
    logger.info(f'获取到的加密结果为：{sign},类型为：{type(sign)}')
    body['key'] = sign
    logger.debug(f'请求地址为：{url}')
    logger.debug(f'请求头为：{header}')
    data_json = json.loads(json.dumps(body))
    logger.debug(f'完整参数为：{data_json}')
    res = requests.post(url=url, json=data_json, headers=header)
    logger.info(f'响应结果为：{res.json()}')

if __name__ == '__main__':
    n = 1
    while True:
        if n < 5:
            ts = int(time.time()) * 1000
            logger.info(f'当前时间戳为：{ts}')
            reqId = str(uuid.uuid1())
            logger.info(f'当前uuid为：{reqId}')
            param = {
                "appId": 10031,
                "key": key_values['10031'],
                "parkId": "210037159",
                "reqId": reqId,
                "serviceCode": "getCarCardList",
                "ts": ts,
                "pageIndex": 1,
                "pageSize": 1,
                "carType": 6,
                "sortField": 0,
                "sortType": 0
            }
            res = TYDW_sign(param)
            logger.info(f'signvalue值为：{res}')
            time.sleep(2)
            logger.info('*********************')
            n = n + 1
        else:
            break