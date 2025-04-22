import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print("Client is Starting....")


port = 5000
client.connect(('localhost',port))
print(f"Client Started at port {port}")
print("Enter the message You Want to send (exit to end the conn)")


while True:
   input_message = input("[Client]: ")
   client.send(input_message.encode())
   if input_message.lower() == 'exit':
       print("[Client] : Ended the Chat.....")
       break
#   to send message
   server_message=client.recv(1024).decode()
   if server_message.lower() == 'exit':
       print("[SERVER] ended the chat.")
       break
   print(f"[Server]: {server_message}")


client.close()



# obv new file
import socket


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


server.bind(('localhost',5000))


print("Server Started at ",5000)


server.listen(1)


conn,adrr=server.accept();


print(f"This is the adddress {adrr}")


while True:


   client_message = conn.recv(1024).decode()
   if client_message.lower() == 'exit':
       print("[Client] ended the chat.")
       break
   print(f"[Client]: {client_message}")


   send_message=input('[SERVER]: ')
   if send_message.lower()=='exit':
       break;
   conn.send(send_message.encode())


conn.close()
server.close()
