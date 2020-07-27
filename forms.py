from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length

class SignupForm(FlaskForm):
	name = StringField('User name', validators=[DataRequired()]) #, Length(min=3, max=50, message="Nombre incorrecto")])
	password = PasswordField('Password', validators=[DataRequired()]) #, Length(min=8, max=30, message="Contraseña invalida")])
	apellidos = StringField('Apellidos', validators=[DataRequired(), Length(min=3, max=80, message="Appellidos Incorrectos")])
	biografia = StringField('biografia', validators=[DataRequired(), Length(min=5, max=80, message="Biografia Incorrecto")])
	correo_electronico = StringField('correo_electronico', validators=[DataRequired(), Length(min=5, max=80, message="Gmail Incorrecto")])	
	numeroTel = StringField('numeroTel', validators=[DataRequired(), Length(min=5, max=80, message="Telefono Incorrecto")])


class LoginForm(FlaskForm):
	name = StringField('User name', validators=[DataRequired(), Length(min=3, max=50, message="Nombre incorrecto")])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30, message="Contraseña invalida")])

class PostForm(FlaskForm):
	descripcion = TextAreaField('Descripcion', validators=[DataRequired()])