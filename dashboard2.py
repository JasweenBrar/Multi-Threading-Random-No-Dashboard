import threading
import tkinter as tk
from tkinter import ttk
import random as r
import time

def display(num, displayLocation):
    # Update label with the generated number at the specified display location
    label = label_dict[displayLocation]
    label.config(text=f"Number: {num}")

def task(lb, ub, refreshTime, displayLocation):
    while True:
        num = r.randint(lb, ub)
        display(num, displayLocation)
        time.sleep(refreshTime)

# Create tkinter window
root = tk.Tk()
root.title("Dashboard")

# Create label dictionary to store labels for display locations
label_dict = {}

# Create labels for display locations
locations = ["Location1", "Location2", "Location3", "Location4", "Location5", "Location6"]
colors = ["red", "blue", "green", "purple", "purple", "red"]
bg_color = "#E6E6FA"
for i, location in enumerate(locations):
    row = i // 2
    col = i % 2
    label = ttk.Label(root, text=f"{location}: N/A", foreground="black", background=bg_color, font=("Arial", 20, "bold"))
    label.grid(row=row, column=col, padx=20, pady=20, sticky="nsew")
    label_dict[location] = label

# Create threads
random_number_t1 = threading.Thread(target=task, args=(10, 20, 10, "Location1"))
random_number_t2 = threading.Thread(target=task, args=(-10, 10, 20, "Location2"))
random_number_t3 = threading.Thread(target=task, args=(-100, 0, 8, "Location3"))
random_number_t4 = threading.Thread(target=task, args=(0, 20, 12, "Location4"))
random_number_t5 = threading.Thread(target=task, args=(-40, 40, 16, "Location5"))
random_number_t6 = threading.Thread(target=task, args=(100, 200, 14, "Location6"))

# Start threads
random_number_t1.start()
random_number_t2.start()
random_number_t3.start()
random_number_t4.start()
random_number_t5.start()
random_number_t6.start()

# Run tkinter event loop
root.mainloop()
