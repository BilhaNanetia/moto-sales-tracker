from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import datetime
import os

template_dir = os.path.abspath('../frontend/templates')
static_dir = os.path.abspath('../frontend/static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a random secret key

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

def get_db_connection():
    db_path = os.path.abspath('../sales_record.db')  # Use an absolute path for the database
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    if user:
        return User(user['id'], user['username'], user['password'])
    return None

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        if user:
            flash('Username already exists')
            return redirect(url_for('signup'))
        hashed_password = generate_password_hash(password)
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        conn.close()
        flash('Account created successfully')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        if user and check_password_hash(user['password'], password):
            user_obj = User(user['id'], user['username'], user['password'])
            login_user(user_obj)
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html')

class SalesRecord:
    def __init__(self, db_name=os.path.abspath('../sales_record.db')):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def add_sale(self, item, quantity, price):
        date = datetime.date.today().isoformat()
        self.cursor.execute('''
            INSERT INTO sales (date, item, quantity, price)
            VALUES (?, ?, ?, ?)
        ''', (date, item, quantity, price))
        self.conn.commit()

    def get_daily_total(self, date):
        self.cursor.execute('''
            SELECT SUM(quantity * price)
            FROM sales
            WHERE date = ?
        ''', (date,))
        result = self.cursor.fetchone()[0]
        return result if result else 0

    def get_daily_sales(self, date):
        self.cursor.execute('''
            SELECT item, quantity, price
            FROM sales
            WHERE date = ?
        ''', (date,))
        return self.cursor.fetchall()

record = SalesRecord()

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/add_sale', methods=['POST'])
def add_sale():
    data = request.json
    record.add_sale(data['item'], data['quantity'], data['price'])
    return jsonify({'success': True})

@app.route('/get_daily_total', methods=['GET'])
def get_daily_total():
    date = request.args.get('date')
    total = record.get_daily_total(date)
    return jsonify({'total': total})

@app.route('/get_daily_sales', methods=['GET'])
def get_daily_sales():
    date = request.args.get('date')
    sales = record.get_daily_sales(date)
    return jsonify({'sales': sales})

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
