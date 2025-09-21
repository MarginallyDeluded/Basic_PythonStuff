import tkinter as tk
from tkinter import ttk

# tk.END represents the end of the current content in a widget.

root = tk.Tk()
root.title("First simple app!")

# lbl = tk.Label(root, text="Label 1")
# lbl.grid(row=0, column=1)

def on_Click():
    print("Cool dude!")

# Create a simple widget
# btn1 = tk.Button(root, text="Button 1", command=on_Click)
# Use a geometry manager to add it to the window
# btn1.grid(row=1, column=2)

def add_to_list(event=None):
    text = entry.get() # get the text from entry
    
    if text:
        text_lst.insert(tk.END, text)
        entry.delete(0, tk.END)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# Frame is a container that allows us to hold more widgets and oganize our layouts.
frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)
btn2 = ttk.Button(root, text="Exit", command=exit)
btn2.grid(row=1, column=1, padx=3)

frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

entry = ttk.Entry(frame)
entry.grid(row=0, column=0, sticky="ew")
entry.bind("<Return>", add_to_list)

entry_btn = ttk.Button(frame, text="Add", command=add_to_list)
entry_btn.grid(row=0, column=1)

text_lst = tk.Listbox(frame)
text_lst.grid(row=1, column=0, columnspan=2, sticky="nsew")

root.mainloop()
