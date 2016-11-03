#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/10/28 上午11:46
from qiniu import Auth, put_file, etag
import time
import hashlib
import pyperclip
import os
def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()


#需要填写你的 Access Key 和 Secret Key,图片储存路径,填写绝对路径,domain七牛云上能看到
image_store='/Users/komgminhao/.image/'
access_key = 'rhMMU4x4W4mmZoGrzryE9pnOVOilQ1euXd8M_JEi'
secret_key = 'gNpt974aebfZy0XJzknErbC7geoNK2z5b7BoiSC5'
domain = 'http://ofqm89vhw.bkt.clouddn.com'
bucket_name = 'image'
#构建鉴权对象
q = Auth(access_key, secret_key)

#上传到七牛后保存的文件名
local_time = str(time.time())
key = md5(local_time)
key = key+'.png'
os.system("/usr/loacl/bin/pngpaste "+image_store+key)
#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)

#要上传文件的本地路径
localfile = image_store+key

ret, info = put_file(token, key, localfile)
pyperclip.copy('![]'+'('+domain+'/'+key+')')
os.remove(image_store+key)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)

