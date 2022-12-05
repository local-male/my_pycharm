# -*- coding: utf-8 -*-
import requests
import json

def res():
    data = {'a':12,'b':12}
    url = 'http://e2gnfk.natappfree.cc/all'
    header = {'content-type':'application/json'}
    dat = requests.post(url = url,headers = header,data = json.dumps(data))
    print(dat)
    print(dat.text)
    #logger.info('接口1' + dat)
res()