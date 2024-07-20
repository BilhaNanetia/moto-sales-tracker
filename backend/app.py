# app.py
from flask import Flask, request, jsonify, render_template
import sqlite3
import datetime
import os


template_dir = os.path.abspath('../frontend/templates')
static_dir = os.path.abspath('../frontend/static')


app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

class SalesRecord:
    def __init__(self, db_name='sales_record.db'):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                item TEXT,
                quantity INTEGER,
                price REAL
            )
        ''')
        self.conn.commit()

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

if __name__ == '__main__':
    app.run(debug=True)