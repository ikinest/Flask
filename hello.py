from flask import Flask # import Flask
app = Flask(__name__) # init a Flask class by a fix parameter __name__

@app.route('/')#homepage view function
def index():
	return '<h1>Hello world!</h1>'

@app.route("/user/<username>") #define a route to parase url
def user(username): # user page
	return '<h1>Hello,%s!</h1>'% username

if __name__ == "__main__":# main function
	app.run(debug = True)#recall flask default server and open debug model
