import tkinter as tk
import window as win
from win32api import GetSystemMetrics

if __name__ == "__main__":
    resolution = str(GetSystemMetrics(0)) + "x" + str(GetSystemMetrics(1))
    root = tk.Tk()
    print("start")
    root.geometry(resolution)
    app = win.Main(root)
    root.mainloop()
