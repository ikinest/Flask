from flask import Flask # import Flask
from flask import request # import request
from flask import make_response # import make_response
from flask_script import Manager
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask import session
from flask import url_for
from flask import redirect
from flask import flash

app = Flask(__name__) # init a Flask class by a fix parameter __name__
app.config['SECRET_KEY'] = '1357999'#avoid CSRF
manager = Manager(app)
bst = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')


@app.route('/',methods=['GET','POST'])#homepage view function
def index():
	form = NameForm()
	if form.validate_on_submit():
		oldname = session.get('name')
		if oldname is not None and oldname != form.name.data:
			flash("Looks you have changed your name.")
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('index'))
	return render_template('index.html',current_time=datetime.utcnow(),form=form ,name=session.get('name'))

@app.route("/user/<username>") #define a route to parase url
def user(username): # user page
	return render_template('user.html',name=username)#name is a variable in user.html

@app.route("/response/")
def genResponse():
	response = make_response("<h1>This is a response object!</h1>")
	response.set_cookie('ikinest','100')
	return response

@app.errorhandler(404)
def pageNotFound(e):
	return render_template('404.html'),404

@app.errorhandler(500)
def Inner_server_error(e):
	return render_template('500.html'),500





if __name__ == "__main__":# main function
	manager.run()#recall flask default server and open debug model
