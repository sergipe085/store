from cs50 import SQL
from flask import Flask, render_template, redirect, request, session
from flask_session import Session

#create app
app = Flask(__name__)

#configure app
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False