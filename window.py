import tkinter as tk


class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="#2d2d2d")
        self.parent = parent
        self.initUI()
    # self.btn = tk.Button(self, text="Check", command=lambda: print("work!"))
    # self.btn.grid(column=0, row=0)
    def initUI(self):
        self.parent.title("Диспетчерское логирование")
        self.pack(fill=tk.BOTH, expand=1)
