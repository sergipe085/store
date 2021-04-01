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

        add(id)

    #GET
    books = []
    for i in session['cart']:
        book = db.execute("SELECT * FROM books WHERE id = (?)", i['id'])
        books.append({
            "name": book[0]['name'],
            "amount": i['amount']
        })

    return render_template('cart.html', books=books)

def add(id):
    for a in session['cart']:
        if a['id'] and a['amount'] and a['id'] == id:
            a['amount'] += 1
            return
    session['cart'].append({
        "id": id,
        "amount": 1
    })