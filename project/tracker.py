from db import add_transaction, fetch_transactions, delete_transaction_by_id
from datetime import datetime

def add_income(amount, category, date=None):
    if not date:
        date = datetime.now().isoformat()
    add_transaction(amount, "Доход", category, date)

def add_expense(amount, category, date=None):
    if not date:
        date = datetime.now().isoformat()
    add_transaction(amount, "Расход", category, date)

def list_transactions():
    return fetch_transactions()

def delete_transaction(trans_id):
    delete_transaction_by_id(trans_id)

def get_balance():
    transactions = list_transactions()
    balance = 0
    for _, amount, t_type, _, _ in transactions:
        if t_type == "Доход":
            balance += amount
        elif t_type == "Расход":
            balance -= amount
    return balance