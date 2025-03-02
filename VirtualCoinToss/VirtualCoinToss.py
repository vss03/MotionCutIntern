import random
import tkinter as tk
from tkinter import messagebox

def flip_coin():
    return random.choice(["Heads", "Tails"])

def update_results():
    global total_flips, heads_count, tails_count
    heads_percentage = (heads_count / total_flips) * 100 if total_flips else 0
    tails_percentage = (tails_count / total_flips) * 100 if total_flips else 0
    result_label.config(text=f"Heads: {heads_count} ({heads_percentage:.2f}%)\nTails: {tails_count} ({tails_percentage:.2f}%)")

def toss_coin():
    global total_flips, heads_count, tails_count, history
    try:
        num_flips = int(entry.get())
        if num_flips <= 0:
            messagebox.showerror("Error", "Please enter a positive number.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a number.")
        return
    
    session_heads = 0
    session_tails = 0
    
    for _ in range(num_flips):
        result = flip_coin()
        if result == "Heads":
            session_heads += 1
            heads_count += 1
        else:
            session_tails += 1
            tails_count += 1
    
    total_flips += num_flips
    history.append(f"Session: Heads={session_heads}, Tails={session_tails}")
    update_results()
    history_label.config(text="\n".join(history[-5:]))

def reset():
    global total_flips, heads_count, tails_count, history
    total_flips = 0
    heads_count = 0
    tails_count = 0
    history = []
    update_results()
    history_label.config(text="")

total_flips = 0
heads_count = 0
tails_count = 0
history = []

# GUI Setup
root = tk.Tk()
root.title("Virtual Coin Toss")

tk.Label(root, text="Enter the number of flips:").pack()
entry = tk.Entry(root)
entry.pack()

toss_button = tk.Button(root, text="Toss Coin", command=toss_coin)
toss_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack()

result_label = tk.Label(root, text="Heads: 0 (0.00%)\nTails: 0 (0.00%)")
result_label.pack()

history_label = tk.Label(root, text="", justify="left")
history_label.pack()

root.mainloop()
