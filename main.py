import tkinter as tk

root = tk.Tk()
root.title("Simple GUI")
root.geometry("300x200")
root.resizable(False, False)

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack()

root.mainloop()