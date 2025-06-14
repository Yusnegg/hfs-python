from tkinter import *
from tkinterdnd2 import DND_FILES, TkinterDnD

PORT = 8000


def start_server():
    print("Server run port {PORT}")

def on_drop(event):
    print("📂 Dropped files:", event.data)

root = TkinterDnD.Tk()
root.title("Simple HFS")
root.geometry("350x400")
root.resizable(False, False)

label = Label(root, text="Drop files here", bg="lightgray", width=40, height=10)
label.pack(padx=10, pady=10)

# Register label as a drop target
label.drop_target_register(DND_FILES)
label.dnd_bind('<<Drop>>', on_drop)

info_label = Label(root, text="", fg="green")
info_label.pack()

root.mainloop()