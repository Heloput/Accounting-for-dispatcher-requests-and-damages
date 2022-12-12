import tkinter as tk
import window as win

if __name__ == "__main__":
    root = tk.Tk()
    print("start")
    root.geometry("250x150")
    app = win.Main(root)
    root.mainloop()
