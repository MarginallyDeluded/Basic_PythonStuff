import tkinter as tk
from tkinter import ttk


def main():
    app = Application()
    app.mainloop()


class InputForm(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=0, sticky="ew")
        self.entry.bind("<Return>", self.add_to_list)

        self.entry_btn = ttk.Button(self, text="Add", command=self.add_to_list)
        self.entry_btn.grid(row=0, column=1)

        self.text_lst = tk.Listbox(self)
        self.text_lst.grid(row=1, column=0, columnspan=2, sticky="nsew")

    def add_to_list(self,event=None):
        text = self.entry.get() # get the text from entry

        if text:
            self.text_lst.insert(tk.END, text)
            self.entry.delete(0, tk.END)


class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Simple App")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        frame = InputForm(self)
        frame.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)

        frame_ = InputForm(self)
        frame_.grid(row=0, column=1, sticky="nsew", padx=3, pady=3)

        self.exit_btn = ttk.Button(self, text="Exit", command=exit)
        self.exit_btn.grid(row=1, column=1)
 

if __name__ == "__main__":
    main()

