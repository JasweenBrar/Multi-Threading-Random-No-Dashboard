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
bg_colors = ["#FFC0CB", "#ADD8E6", "#90EE90", "#FFFFE0", "#DDA0DD", "#FFA07A"]
for i, location in enumerate(locations):
    row = i // 2
    col = i % 2
    label = ttk.Label(root, text=f"Number: N/A", font=("Helvetica", 16), foreground="black", background=bg_colors[i])
    label.grid(row=row, column=col, padx=20, pady=20, sticky="nsew")
    label_dict[location] = label

# Create threads
random_number_t1 = threading.Thread(target=task, args=(10, 20, 1, "Location1"))
random_number_t2 = threading.Thread(target=task, args=(-10, 10, 2, "Location2"))
random_number_t3 = threading.Thread(target=task, args=(-100, 0, 3, "Location3"))
random_number_t4 = threading.Thread(target=task, args=(0, 20, 4, "Location4"))
random_number_t5 = threading.Thread(target=task, args=(-40, 40, 5, "Location5"))
random_number_t6 = threading.Thread(target=task, args=(100, 200, 6, "Location6"))

# Start threads
random_number_t1.start()
random_number_t2.start()
random_number_t3.start()
random_number_t4.start()
random_number_t5.start()
random_number_t6.start()

# Set grid weights
for i in range(len(locations)):
    root.grid_rowconfigure(i // 2, weight=1)
    root.grid_columnconfigure(i % 2, weight=1)

# Run tkinter event loop
root.mainloop()
