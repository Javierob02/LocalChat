#-------------------------------------------------------------------------------------#
#-------------------------- Server Side For 'LocalChat' ------------------------------#
#-------------------------------------------------------------------------------------#

import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Server IP address
PORT = 13333 # Non-Service port used for Server - Client communication

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

# List to store client connections
client_connections = []
client_usernames = []

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                if message == '[USERS]':
                    client_socket.send(f'Connected Users: {client_usernames}'.encode('utf-8'))
                else:
                    broadcast_message = f'{username} > {message}'
                    print(broadcast_message)
                    broadcast(broadcast_message, client_socket)
            else:
                remove_client(client_socket, username)
                break
        except Exception as e:
            print(f"Error: {e}")
            remove_client(client_socket, username)
            break

def broadcast(message, sender_socket):
    for client in client_connections:
        if client != sender_socket:
            client.send(message.encode('utf-8'))

def remove_client(client_socket, username):
    index = client_connections.index(client_socket)
    client_connections.remove(client_socket)
    client_socket.close()

    removed_username = client_usernames[index]
    client_usernames.remove(removed_username)
    broadcast(f'[-] {removed_username} has left the chat', None)
    
def accept_connections():
    while True:
        client_socket, client_address = server_socket.accept()

        username = client_socket.recv(1024).decode('utf-8')
        client_connections.append(client_socket)
        client_usernames.append(username)

        print(f"New connection from {client_address} > ('{username}')")
        broadcast(f'[+] {username} has joined the chat', None)
        client_socket.send('\tWelcome to the chat!'.encode('utf-8'))

        client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
        client_thread.start()



#---------------- Main() ----------------
# Start accepting connections
accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()
print(f'Host: {HOST} open on Port: {PORT} ...')