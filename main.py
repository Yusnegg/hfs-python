from tkinter import *
from tkinterdnd2 import DND_FILES, TkinterDnD

def on_drop(event):
    print("📂 Dropped files:", event.data)

root = TkinterDnD.Tk()
root.title("Simple GUI")
root.geometry("300x200")
root.resizable(False, False)

label = Label(root, text="Drop files here", bg="lightgray", width=40, height=10)
label.pack(padx=10, pady=10)

# Register label as a drop target
label.drop_target_register(DND_FILES)
label.dnd_bind('<<Drop>>', on_drop)

root.mainloop()