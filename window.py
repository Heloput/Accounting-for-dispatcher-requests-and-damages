import tkinter as tk


class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="#2d2d2d")
        self.btn = tk.Button(self, text="Файл", command=lambda: print("work!"), bg="#F8FAFC", fg="#344054")
        self.parent = parent
        self.initUI()


    def initUI(self):
        self.parent.title("Диспетчерское логирование")
        self.pack(fill=tk.BOTH, expand=1)
        self.btn.grid(column=0, row=0)
