import tkinter as tk
from tkinter import ttk
from gui import create_gui

def main():
    root = tk.Tk()
    root.title("Printing Services Details")
    create_gui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
