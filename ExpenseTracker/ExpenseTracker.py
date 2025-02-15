import json
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox

# Data file path
DATA_FILE = 'expenses.json'

# Load existing data
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save data to file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Add a new expense
def add_expense():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get().strip().lower()
        description = description_entry.get()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        expenses.append({'amount': amount, 'category': category, 'description': description, 'date': date})
        save_data(expenses)
        messagebox.showinfo("Success", "Expense added successfully!")
        clear_entries()
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid amount.")

# View expense summary
def view_summary():
    total_expense = sum(exp['amount'] for exp in expenses)
    summary_text.set(f"Total Expense: {total_expense:.2f}")

    category_expenses = {}
    for exp in expenses:
        category = exp['category']
        category_expenses[category] = category_expenses.get(category, 0) + exp['amount']

    summary_details = "Category-wise Expenditure:\n"
    for category, amount in category_expenses.items():
        summary_details += f"  {category}: {amount:.2f}\n"

    summary_label.config(text=summary_details)

# Clear input entries
def clear_entries():
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

# Initialize data
expenses = load_data()

# Create the main window
root = tk.Tk()
root.title("Expense Tracker")

# Create input fields
tk.Label(root, text="Amount:").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="Category:").grid(row=1, column=0)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1)

tk.Label(root, text="Description:").grid(row=2, column=0)
description_entry = tk.Entry(root)
description_entry.grid(row=2, column=1)

# Create buttons
add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

view_button = tk.Button(root, text="View Summary", command=view_summary)
view_button.grid(row=4, column=0, columnspan=2, pady=10)

# Create summary display
summary_text = tk.StringVar()
summary_label = tk.Label(root, textvariable=summary_text, justify=tk.LEFT)
summary_label.grid(row=5, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
