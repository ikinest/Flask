from flask import Flask # import Flask
from flask import request
app = Flask(__name__) # init a Flask class by a fix parameter __name__

@app.route('/')#homepage view function
def index():
	User_Agent = request.headers.get('User-Agent')
	return '<h1>Your browser is %s</h1>' % User_Agent 

@app.route("/user/<username>") #define a route to parase url
def user(username): # user page
	return '<h1>Hello,%s!</h1>'% username


if __name__ == "__main__":# main function
	app.run(debug = True)#recall flask default server and open debug model
