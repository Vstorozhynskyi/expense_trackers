# Expense Tracker
import csv
expenses = []
def add_expense(name, amount): expenses.append([name, amount])
def save_expenses(): open("expenses.csv", "w").writelines(["name,amount\n"] + [f"{n},{a}\n" for n, a in expenses])
while True:
    cmd = input("Enter command (add/save/exit): ")
    if cmd == "add": add_expense(input("Name: "), input("Amount: "))
    elif cmd == "save": save_expenses(); print("Saved!")
    elif cmd == "exit": break
