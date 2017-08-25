# Flask Web Development Writingscripts

# 第一部分：Flask 基础
<ul>
	<li>1a:Flask程序结构</li>
		"""
		from flask import Flask
		app = Flask(__name__)#通过一个默认参数实例化Flask对象		
		
		#注册路由route
		@app.route("/")#HomePage页面将会跳转到此路由下的试图函数（View Function）
		def index():#定义HomePage页面试图函数
			return "<h1>Hello,World</h1>"
		
		#Flask程序入口
		if __name__ == "__main__":
			app.run(debug = True) #启动Flask自动服务器，同时开启调试模式。
		"""
	<li>1b:动态参数</li>
		@app.route(/user/<username>)#通过<username>传递不同的用户名
		def user(username):#试图函数中添加动态参数username
			return '<h1>Hello,%s!</h1>'% username   #解析动态参数
			
</ul>

