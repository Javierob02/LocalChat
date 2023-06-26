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
- The client connects to the server using the provided IP address and port number.
- The client sends its username to the server upon connection.
- The client receives messages from the server and displays them in a chat log area.
- The client can send messages by typing in the input field and pressing the "Send" button or pressing the Enter key.
- The client can request a list of connected users by clicking the "Users" button.
- The client can exit the chat application by clicking the "X" button or pressing the Escape key.
- The client uses the TCP/IP protocol to communicate with the server.

  <img width="924" alt="Image_1" src="https://github.com/Javierob02/LocalChat/assets/93495474/efc9def6-ec34-44dc-906a-4b410a6b7cae">

  <img width="456" alt="Image_2" src="https://github.com/Javierob02/LocalChat/assets/93495474/a5a40701-b146-4503-8cb6-1b99a29e1f56">

  <img width="933" alt="Image_3" src="https://github.com/Javierob02/LocalChat/assets/93495474/8d2afb0b-027b-4301-b876-bb10a79d2457">



