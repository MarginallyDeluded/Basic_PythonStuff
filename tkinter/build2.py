import tkinter as tk
from tkinter import ttk

## Creating Apps using classes

# Method-1
'''
class Application:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple App")
        self.root.mainloop()

app = Application()
'''

# Method-2
'''
class Application:

    def __init__(self,root):
        self.root = root
        self.root.title("Simple App")

root = tk.Tk()
app = Application(root)
root.mainloop()
'''
# Method-3 
# Our subclass Application always gives an instance of its parent class tk.Tk
# so no need to create a root seaparately

def main():
    app = Application()
    app.mainloop()


class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Simple App")

if __name__ = "__main__":
    main()




