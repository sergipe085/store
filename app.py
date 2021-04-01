from cs50 import SQL
from flask import Flask, render_template, redirect, request, session
from flask_session import Session

#create app
app = Flask(__name__)

#configure app
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)

#connect to db
db = SQL('sqlite:///store.db')

@app.route('/')
def index():
    books = db.execute("SELECT * FROM books")
    return render_template('index.html', books=books)

@app.route('/cart', methods=["GET", "POST"])
def cart():
    if "cart" not in session:
        session['cart'] = []

    #POST
    if request.method == 'POST':
        id = request.form.get('id')
        session['cart'].append(id)

    #GET
    books = db.execute("SELECT * FROM books WHERE id IN (?)", session['cart'])
    return render_template('cart.html', books=books)    