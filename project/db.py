import sqlite3
import os

os.makedirs('data', exist_ok=True)

def init_db():
    conn = sqlite3.connect('data/finance.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            amount REAL,
            type TEXT CHECK(type IN ('Доход', 'Расход')),
            category TEXT,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_transaction(amount, t_type, category, date):
    conn = sqlite3.connect('data/finance.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO transactions (amount, type, category, date) VALUES (?, ?, ?, ?)',
                (amount, t_type, category, date))
    conn.commit()
    conn.close()

def fetch_transactions():
    conn = sqlite3.connect('data/finance.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM transactions ORDER BY date DESC')
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_transaction_by_id(trans_id):
    conn = sqlite3.connect('data/finance.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM transactions WHERE id = ?', (trans_id,))
    conn.commit()
    conn.close()
