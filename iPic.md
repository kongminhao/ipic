#ipic workflow 开发遇到的坑233333

1. 图床早就选好了，使用七牛，每月有免费的10GB流量，非常nice
2. 自带python的sdk，api接口也十分方便
3. [python sdk](http://developer.qiniu.com/code/v7/sdk/python.html#install)
4. 有源代码，注意，不支持python3.5，反正workflow也只能用2.7的版本写，我们不管它。
5. 描述下想法，原来想直接上传的，后面发现不行

![](http://ofqm89vhw.bkt.clouddn.com/c89b750bdfcae9ea57184a1d0e259acd.png)

在sdk中有这么一行，描述了上传路径，也就是说不能直接上传，需要存到本地再上传，说实话，这样可能比较慢，但是也没什么办法。


然后就是用python读取剪切板中的内容了，上网一搜，简单嘛，

	from PIL import ImageGrab
	im = ImageGrab.grabclipboard()  


好的，运行一下。

![](http://ofqm89vhw.bkt.clouddn.com/42777e54b43520870b8ec1bf9bc580dd.png)

我日，未实现，真坑。

遂转而寻找其他方案，找到了shell命令以读取剪切板内容的 

pbcopy,pbpaste 

可是也只能读取文本内容，不能读取图片。

在网上找到了个pyobjc库，可是要自己写objective-c

遂到群里询问

描述了一遍需求之后，天少直接抛出了一个网址

[pngpaste](https://github.com/jcsalterego/pngpaste)

呜，感谢天少

好了，有了这个一切问题都好办了，pngpaste 把剪切板内的图片保存到本地。

os.system()执行系统操作

然后调用pythonsdk上传即可

代码瞬间写完加解决

```python
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
```

然后搞进alfred 

这时候出现了真正的大坑

因为当时年少无知，装了很多python

我也忘了所有的python怎么安装的了，我记得brew安装了3个，rpm包装了两个吧，再加系统自带的python，这就是6个了，😨。

然后就是真正的坑了，源码放进去跑，提示，没有moudle

所以千万不要作死

只能一个一个试了

在网上找一找

 	import sys
	path = sys.executable
 	print path

获取安装路径：

一个一个试吧

最后试到了

然后 
	
	当然先做了个备份
	ln -sf python路径 /usr/bin/python 

上帝保佑我，千万别挂。

oyeah，没挂。

跑一跑，有个问题，其实直接用上面的代码是没问题的。

就是python这个账户的权限可能比较低，所以不能直接用shell的命令，需要加上绝对路径

	os.system("/usr/loacl/bin/pngpaste "+image_store+key)

自此，结束，其实主要是python环境的锅，配了好久，所以，千万别作死。




	