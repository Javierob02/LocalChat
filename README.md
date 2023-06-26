# Description
This project is a simple chat application called "LocalChat" implemented using Python and Tkinter for the GUI. It allows users to connect to a server and exchange messages with each other in a local network.

# Server Side
- The server side sets up a socket and listens for client connections on a specified IP address and port number.
- When a client connects, the server accepts the connection, receives the client's username, and adds the client's socket to a list of client connections.
- The server handles each client in a separate thread to enable concurrent communication.
- The server receives messages from clients and broadcasts them to all connected clients, including the username of the sender.
- Clients can request a list of connected users, and the server responds with the list.
- If a client disconnects, the server removes their socket from the list of connections and broadcasts a notification to all clients.
- The server uses the TCP/IP protocol for reliable communication over a network.

![Server_IMG](https://github.com/Javierob02/LocalChat/assets/93495474/e6e956a2-5ef2-4c15-8e58-4b2acb763f95)

# Client Side


# Functionalities
