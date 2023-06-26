#-------------------------------------------------------------------------------------#
#-------------------------- Client Side For 'LocalChat' ------------------------------#
#-------------------------------------------------------------------------------------#

import sys
import socket
import threading
import tkinter as tk
from tkinter import messagebox

# Server configuration
HOST = '127.0.0.1'  # Server IP address
PORT = 13333 # Non-Service port used for Server - Client communication


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            chat_log.insert(tk.END, message + "\n")
        except Exception as e:
            print(f"Error: {e}")
            client_socket.close()
            break

def send_message(client_socket):
    message = entry.get()
    if message.strip() != "":
        if username.strip() != "":
            chat_log.insert(tk.END, f'{username} > {message}\n')
            entry.delete(0, tk.END)
            client_socket.send(message.encode('utf-8'))

def exit_chat(client_socket):
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        client_socket.close()
        root.destroy()

def request_connected_users(client_socket):
    client_socket.send("[USERS]".encode('utf-8'))

def start_chat(username):
    try:
        # Connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))

        client_socket.send(username.encode('utf-8'))

        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()

        send_button.config(command=lambda: send_message(client_socket))
        users_button.config(command=lambda: request_connected_users(client_socket))
        root.bind("<Return>", lambda event: send_message(client_socket))
        root.bind("<Escape>", lambda event: exit_chat(client_socket))
    except Exception as e:
        print(f"Error: {e}")


#------------------------------- GUI -------------------------------

# Check if username is provided as a command-line argument
if len(sys.argv) < 2:
    print("Please provide a username.")
else:
    username = sys.argv[1]

    # Create the main window
    root = tk.Tk()
    root.title("LocalChat")

    # Create the username label
    username_label = tk.Label(root, text=f"Username: {username}")
    username_label.pack()

    # Create the chat log display
    chat_log = tk.Text(root, width=50, height=20)
    chat_log.pack(fill=tk.BOTH, expand=True)

    # Create the message input field
    entry = tk.Entry(root, width=50)
    entry.pack()

    # Create the send button
    send_button = tk.Button(root, text="Send")
    send_button.pack()

    # Show online users
    users_button = tk.Button(root, text="Users")
    users_button.pack()

    # Start the chat client
    start_chat(username)

    # Start the main event loop
    root.mainloop()
