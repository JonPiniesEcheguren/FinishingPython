from flask import Flask, request, url_for

from EjerciciosFlask.appEj06 import appEj06
from EjerciciosFlask.appEj07 import appEj07 
from EjerciciosFlask.appEj08 import appEj08 
from EjerciciosFlask.appEj11 import appEj11 
from EjerciciosFlask.appEj12 import appEj12 
from EjerciciosFlask.appEj13 import appEj13 

app=Flask(__name__)

app.register_blueprint(appEj06)
app.register_blueprint(appEj07)
app.register_blueprint(appEj08)
app.register_blueprint(appEj11)
app.register_blueprint(appEj12)
app.register_blueprint(appEj13)