import matplotlib.pyplot as plt
from db import fetch_transactions
from collections import defaultdict

def plot_income_vs_expense_by_category():
    transactions = fetch_transactions()

    income_by_category = defaultdict(float)
    expense_by_category = defaultdict(float)
    total_income = 0
    total_expense = 0

    for trans in transactions:
        _, amount, t_type, category, _ = trans
        if t_type == "Доход":
            income_by_category[category] += amount
            total_income += amount
        elif t_type == "Расход":
            expense_by_category[category] += amount
            total_expense += amount

    balance = total_income - total_expense

    all_categories = sorted(set(income_by_category.keys()) | set(expense_by_category.keys()))
    income_values = [income_by_category[cat] for cat in all_categories]
    expense_values = [expense_by_category[cat] for cat in all_categories]

    x = range(len(all_categories))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar([i - width/2 for i in x], income_values, width=width, label='Доходы', color='green')
    plt.bar([i + width/2 for i in x], expense_values, width=width, label='Расходы', color='red')

    plt.xticks(ticks=x, labels=all_categories, rotation=45, ha='right')
    plt.ylabel("Сумма")
    plt.title("Доходы и расходы по категориям")

    #отображение баланса
    plt.text(0.95, 0.95, f"Баланс: {balance:.2f} ₽",
             transform=plt.gca().transAxes,
             fontsize=12, color="blue",
             horizontalalignment='right',
             bbox=dict(facecolor='white', edgecolor='blue', boxstyle='round,pad=0.5'))

    plt.legend()
    plt.tight_layout()
    plt.show()
