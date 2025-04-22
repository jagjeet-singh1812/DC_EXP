import socket
import threading


def receive_messages(client_socket):
   while True:
       try:
           message = client_socket.recv(1024).decode()
           print(message)
       except:
           print("[ERROR] Disconnected from server.")
           client_socket.close()
           break


def start_client():
   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   client.connect(('localhost', 6000))


   # Wait for name prompt
   prompt = client.recv(1024).decode()
   print(prompt, end='')  # Print prompt without newline
   name = input()
   client.send(name.encode())


   print(f"{name} Connected to group chat. Type 'exit' to leave.")


   threading.Thread(target=receive_messages, args=(client,), daemon=True).start()


   while True:
       msg = input()
       client.send(msg.encode())
       if msg.lower() == 'exit':
           print("[CLIENT] Exiting chat...")
           client.close()
           break


start_client()











import socket
import threading


clients = {}  # socket -> name
lock = threading.Lock()  # For thread-safe access to 'clients'


def handle_client(client_socket, addr):
   try:
       client_socket.send("Enter your name: ".encode())
       name = client_socket.recv(1024).decode().strip()


       with lock:
           clients[client_socket] = name


       print(f"[SERVER] {name} joined from {addr}")
       broadcast(f"[SERVER] {name} has joined the chat!", client_socket)


       while True:
           message = client_socket.recv(1024).decode()
           if message.lower() == 'exit':
               print(f"[SERVER] {name} left the chat.")
               broadcast(f"[SERVER] {name} has left the chat.", client_socket)
               break
           print(f"[{name}]: {message}")
           broadcast(f"[{name}]: {message}", client_socket)


   except:
       print(f"[ERROR] {addr} disconnected.")


   # Cleanup
   with lock:
       if client_socket in clients:
           del clients[client_socket]
   client_socket.close()


def broadcast(message, sender_socket):
   with lock:
       for client in list(clients):  # Make a copy to avoid modification errors
           if client != sender_socket:
               try:
                   client.send(message.encode())
               except:
                   client.close()
                   del clients[client]


def start_server():
   server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server.bind(('localhost', 6000))
   server.listen()
   print("[SERVER] Group chat server started on port 6000...")


   while True:
       client_socket, addr = server.accept()
       thread = threading.Thread(target=handle_client, args=(client_socket, addr))
       thread.start()


start_server()
