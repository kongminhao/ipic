#ipic翻版使用说明

依赖库有点多，自行安装
	
	pip install qiniu
	pip install requests
	pip install pyperclip
	brew intsall pngpaste//没安装brew的面壁思过去，安装方法不教

配置

![](http://ofqm89vhw.bkt.clouddn.com/0f719dfa6a345789881f55f542770c1c.png)

配置参数在ipic的第二个RunScript中

总共有四个参数需要填写

你也可以不用填写，直接用我的，我觉得也不会出什么问题，10G应该够用了吧。

![](http://ofqm89vhw.bkt.clouddn.com/98d910cba71fa46a5cd5d119049b0f20.png)

acess_key 

secret_key

在七牛云的个人面板的秘钥管理处可以看到

没注册七牛云的小伙伴看这里

[点击注册](https://portal.qiniu.com/signup?code=3lhweqbicuzbm)

通过这个注册能给送本人一丢丢免费流量，如果你不想用也不勉强，你可以自
行前往七牛官网注册

bucket_name 

domain 

![](http://ofqm89vhw.bkt.clouddn.com/2b114e0514ef5b27a6a9f03d20e440b0.png)

点击对象存储下面的立即添加

![](http://ofqm89vhw.bkt.clouddn.com/a16b223a9c752e1b42f861b9bbe12838.png)

假设我这里令空间名字为test，那么配置里写bucket_name 就写test
，这里请看清楚你的存储区域，最好写离你比较近的节点，访问限制务必选择公开空间。

点击确认创建

![](http://ofqm89vhw.bkt.clouddn.com/8b15647878ed15dfdb2c73f4a111af98.png)

之后你能看见一个测试域名，把它复制下来

比如我这个是


ofr0necj4.bkt.clouddn.com

那么domain就写成

http://ofr0necj4.bkt.clouddn.com

有任何bug或者issues欢迎提交 


copyright © Scu_laji




	