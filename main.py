import http.server
import socketserver
import threading
from tkinter import *
import os
from tkinterdnd2 import DND_FILES, TkinterDnD

PORT = 8000
server_thread = None
httpd = None

def start_server(folder_path):
    global server_thread, httpd

    os.chdir(folder_path)

    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), handler)

    def server_loop():
        print(f"Server run port {PORT}")
        httpd.serve_forever()

    server_thread = threading.Thread(target=server_loop, daemon=True)
    server_thread.start()

def on_drop(event):
    folder = event.data.strip("{}")
    if not folder:
        info_label.config(text="No files dropped")
        return
    else:
        info_label.config(text="Files dropped")
        start_server(folder)

    print("📂 Dropped files:", event.data)

root = TkinterDnD.Tk()
root.title("Simple HFS")
root.geometry("350x300")
root.resizable(False, False)

label = Label(root, text="Drop files here", bg="lightgray", width=40, height=10)
label.pack(padx=10, pady=10)

# Register label as a drop target
label.drop_target_register(DND_FILES)
label.dnd_bind('<<Drop>>', on_drop)

info_label = Label(root, text="", fg="green")
info_label.pack()

root.mainloop()