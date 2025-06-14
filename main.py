# ===============================================================
# Simple HTTP File Server with Drag & Drop GUI
# Author: _bkir0
# License: MIT
# Description:
#   This script provides a Tkinter-based GUI to drag & drop a folder
#   and start an HTTP server on the specified port to serve its contents.
# ===============================================================

import http.server
import socketserver
import threading
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
import os
from tkinterdnd2 import DND_FILES, TkinterDnD

server_thread = None
httpd = None
server_url = None

def start_server(folder_path, port):
    """
    Starts the HTTP server to serve the selected folder on the given port.
    """
    global server_thread, httpd, server_url

    try:
        port = int(port)
    except ValueError:
        showerror("Invalid Port", "Please enter a valid numeric port.")
        return

    os.chdir(folder_path)

    handler = http.server.SimpleHTTPRequestHandler

    try:
        httpd = socketserver.TCPServer(("", port), handler)
    except OSError:
        showerror("Port Error", f"Port {port} is already in use.")
        return

    def server_loop():
        print(f"🌐 Server running on http://localhost:{port}/")
        httpd.serve_forever()

    server_thread = threading.Thread(target=server_loop, daemon=True)
    server_thread.start()

    server_url = f"http://localhost:{port}/"
    info_label.config(text=f"✅ Server is running at {server_url}")
    open_btn.config(state=NORMAL)

def on_drop(event):
    """
    Triggered when a folder is dropped into the drop zone.
    Validates the folder and starts the server.
    """
    folder = event.data.strip("{}")
    port = port_var.get()

    if not folder or not os.path.isdir(folder):
        info_label.config(text="❌ Invalid folder dropped.")
        return

    start_server(folder, port)
    print("📂 Dropped folder:", folder)

def open_browser():
    """
    Opens the current server URL in the default web browser.
    """
    if server_url:
        webbrowser.open(server_url)

# ===== GUI Setup =====
root = TkinterDnD.Tk()
root.title("🔧 Simple HTTP Server by _bkir0")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Styling
style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10))

# Title label
title = Label(root, text="🚀 Drag & Drop a Folder to Start Server", bg="#f0f0f0", font=("Segoe UI", 12, "bold"))
title.pack(pady=10)

# Port input section
port_frame = Frame(root, bg="#f0f0f0")
port_frame.pack(pady=5)

Label(port_frame, text="Port:", bg="#f0f0f0").pack(side=LEFT, padx=5)
# Input field bound to port_var
port_var = StringVar(value="8000")
port_entry = Entry(port_frame, textvariable=port_var, width=10)
port_entry.pack(side=LEFT)

# Drop area
drop_zone = Label(root, text="📂 Drop a folder here", bg="lightgray", fg="black",
                  width=40, height=10, relief=RIDGE, borderwidth=2)
drop_zone.pack(pady=15)

drop_zone.drop_target_register(DND_FILES)
drop_zone.dnd_bind('<<Drop>>', on_drop)

# Info label
info_label = Label(root, text="", fg="green", bg="#f0f0f0", font=("Segoe UI", 10, "italic"))
info_label.pack(pady=10)

# Open browser button (disabled until server starts)
open_btn = Button(root, text="🌐 Open in browser", state=DISABLED, command=open_browser)
open_btn.pack(pady=10)

# Main loop
root.mainloop()
