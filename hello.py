from flask import Flask # import Flask
app = Flask(__name__) # init a Flask class by a fix parameter __name__

@app.route("/") #define a route to parase url
def index(): # homepage view function
	return '<h1>Hello World!</h1>'

if __name__ == "__main__":# main function
	app.run(debug = True)#recall flask default server and open debug model
