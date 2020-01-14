import random
import requests
from django.core.cache import cache

from common.api import YZX_PARAMS,YZX_URL
from common import keys

def generate_vcode(length=6):
    return "".join([str(random.randint(0,9)) for i in range(length)])

def send_vcode(phonenum):
    params=YZX_PARAMS.copy()
    vcode=generate_vcode()
    params["mobile"]=phonenum
    params["param"]=vcode
    response=requests.post(url=YZX_URL,json=params)
    if response.status_code==200:
        if response.json()["msg"]=="账号未认证":
            cache.set(keys.VCODE_KEY % phonenum,vcode,180)
            return True
        return False
    return False
