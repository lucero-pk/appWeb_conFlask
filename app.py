import datetime
import uuid
import os

from flask import Flask, render_template, redirect, url_for, session, flash

from flask_session import Session

from pymongo import MongoClient
from redis import Redis

from forms import *  

mongo = MongoClient("mongodb://bdd_mongo:27017/")
mongodb = mongo.testdb

redis = Redis(host="bdd_redis")

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis

Session(app)

@app.route("/", methods=["GET", "POST"])
def timeline():

	form = PostForm()
	if form.validate_on_submit():
		post = {
			'descripcion': form.descripcion.data
			'user_id': user['_id']
		}

		mongodb.posts.insert_one(post)
		return str(post)

	#consultar los datos de las publicaciones 
	posts = list(mongodb.posts.find())
	
	#print(posts)
	#for post in posts:
		#post['user'] = mongodb.users.find_one({'_id': post['user_id']})

	user = session.get('profile')
	if not user:
		return redirect(url_for('login'))

	return render_template('home.html', user=user, form=form, posts=posts)

@app.route("/signup", methods=["GET", "POST"])
def signup():
	form = SignupForm()
	
	if form.validate_on_submit():
		user = {
			#'user_id': user['_id'] #user del usuario
			'name': form.name.data,
			'password': form.password.data,
			'apellidos': form.apellidos.data,
			'biografia': form.biografia.data,
			'correo_electronico':form.correo_electronico.data, 
			'numeroTel' : form.numeroTel.data			
			#return "usuario: %s contraseña: %s" % (name, password)
		}

		mongodb.users.insert_one(user)
		return redirect(url_for("login"))
		#mongodb.users.insert_one(user)
		#return str(user)

	return render_template("signup.html", form=form)
	#return "Resgistrarse al sistema"

@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		user = mongodb.users.find_one({
			'name': form.name.data,
			'password': form.password.data
	
		})

		if not user:
			flash('Invalid user/password')
			return redirect(url_for('login'))

		session['profile'] = user
		return redirect(url_for('timeline'))

		#else:
			#return "Acceso correcto!"

	return render_template("login.html", form=form)

@app.route("/logout")
def logout():
	session['profile'] = None
	return redirect(url_for('timeline'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5090, debug=True)
