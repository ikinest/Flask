__author__="ikinest"
from flask import Flask # import Flask
from flask import make_response
from flask import redirect
from flask import abort
app = Flask(__name__) # init a Flask class by a fix parameter __name__

@app.route('/')#homepage view function
def index():
	#return "<h1>Bad Request!</h1>",400
	#-------------	
	response = make_response('<h1>This document carries a cookie!</h1>')
	response.set_cookie('ikinest','100')
	return response
	#------------
	#return redirect('http://www.google.com/')
	#--------
	
@app.route("/user/<username>") #define a route to parase url
def user(username): # user page
	return '<h1>Hello,%s!</h1>'% username

@app.route('/getuser/<id>')
def get_user(id):
	abort(404)
	

if __name__ == "__main__":# main function
	app.run(debug = True)#recall flask default server and open debug model
