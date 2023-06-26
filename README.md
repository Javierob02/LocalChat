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

![Server_IMG](https://github.com/Javierob02/LocalChat/assets/93495474/3355930a-5229-4a15-95ad-05d9d7fb3c13)


# Client Side
- The client connects to the server using the provided IP address and port number.
- The client sends its username to the server upon connection.
- The client receives messages from the server and displays them in a chat log area.
- The client can send messages by typing in the input field and pressing the "Send" button or pressing the Enter key.
- The client can request a list of connected users by clicking the "Users" button.
- The client can exit the chat application by clicking the "X" button or pressing the Escape key.
- The client uses the TCP/IP protocol to communicate with the server.

![IMG_1](https://github.com/Javierob02/LocalChat/assets/93495474/a528310b-117c-477a-b9a1-31a8fe29245e)
![IMG_2](https://github.com/Javierob02/LocalChat/assets/93495474/c5e75669-1825-4725-af3a-7fadedd89f31)
![IMG_3](https://github.com/Javierob02/LocalChat/assets/93495474/d7eee4e5-6bce-44b6-b465-0c2c69b1c067)

# Libraries Used

#### Server Side:

- **socket**: Provides the necessary functionality for socket programming, enabling network communication.
- **threading**: Used to handle multiple client connections concurrently with threads.

#### Client Side:

- **socket**: Used for client-server communication over the network.
- **threading**: Employed to receive messages from the server asynchronously.
- **tkinter**: Provides the graphical user interface (GUI) components for building the chat client application.
- **sys**: Used to access command-line arguments to retrieve the username.
- **messagebox**: Utilized for displaying a confirmation dialog when exiting the chat client.

# Execution of application

#### Server -> python3 ./Server_LocalChat.py 

#### Client -> python3 ./LocalChat `<username>`



