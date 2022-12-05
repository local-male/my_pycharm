# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/9/23 16:16:31
import hashlib
import time
import uuid
from keytop.log_utils import logger

#统一对外接口加密
def TYDW(param):
    ''
    '''lianxi、将json的所有非空属性名(属性值不为null且不为空字符串以及appId与appSercert除外)ASCII码从小到大排序（字典序），
    使用URL键值对的格式（即key1=value1&key2=value2…）拼接成字符串stringA；注意（参数为空值、json对象、数组的，不参与加密）
    2、stringA用“&”拼接上appSercert得到stringSignTemp字符串，并对stringSignTemp进行MD5运算，再将得到的字符串所有字符
    转换为大写，得到sign值signValue'''

    '''第一步：获取到需要处理的参数body（字典格式）'''
    url = 'http://tsktapps.keytop.cn/unite-api/api/wec/GetCarCardInfo'
    param = {"appId": "10031","key": "{{key}}","parkId": "210037159","reqId": '{{reqId}}',
             "serviceCode": "getCarCardInfo","ts": "{{ts}}","cardId":1,"state":0}

    '''第二步：将参数body中的所有参数按照ascll码排序'''
    sort_1 = sorted(param.items() ,key=lambda x :x[0])
    logger.debug(f'排序后的body为：{sort_1},类型为：{type(sort_1)}')

    '''第三步：将排序后的值转换为字典'''
    sort_2 = dict(sort_1)
    logger.debug(f'{sort_2}')

    '''第四步：去掉字典value为null、空、appSercert、json对象、数组
              新建一个空字符串，将不满足条件的参数去除之后的body进行拼接'''
    sort_3 = ''
    for key,value in sort_2.items():
        if isinstance(value,list) or isinstance(value,dict) or (value==None) or \
                (value == '') or isinstance(value,int) or (key == 'appId'):
            continue
        sort_3 = sort_3 + key + '=' + str(value) + '&'
    logger.debug(f'参数拼接之后的结果为：{sort_3}，类型为：{type(sort_3)}')
    sort_4 = sort_3[:-1]
    logger.debug(f'参数拼接之后去除&的结果为：{sort_4}，类型为：{type(sort_4)}')

    '''第五步：拼接appSercert 值'''
    appSercert = '9d682649d9f64faeb5e4477a8e27858e'
    sort_5= sort_4 + '&' + appSercert
    logger.debug(f'拼接appSercert后的字符串为：{sort_5}，类型为：{type(sort_5)}')

    '''第六步：进行md5加密'''
    sort_5 = hashlib.md5()
    sort_5.update(str.encode("utf8"))
    logger.info(f'md5加密后的值为：{sort_5.hexdigest()}')

    '''第七步：转换为大写'''
    sign = sort_5.hexdigest().upper()
    logger.debug(f'转换为大写后的值为：{sign}')


    '''获取ts 当前时间戳
    print (ts)                           #原始时间数据
    print (int(ts))                      #秒级时间戳
    print (int(round(ts * 1000)))        #毫秒级时间戳
    print (int(round(ts * 1000000)))     #微秒级时间戳'''
    ts = int(time.time()) *1000
    logger.info(f'当前时间的时间戳为：{ts}')

    '''获取reqId：唯一标识'''
    reqId = uuid.uuid1()
    logger.debug(f'uuid唯一标识为：{reqId}')



if __name__ == '__main__':
    reqId = uuid.uuid1()
    time.sleep(1)
    print(reqId)
    ts = int(time.time()) * 1000
    # param = {"appId": "10031","key": "{{key}}","parkId": "210037159","reqId": reqId,
    #           "serviceCode": "getCarCardInfo","ts": ts,"cardId":lianxi,"state":0}
    # sign = test_TYDW(param)
    # print(sign)
