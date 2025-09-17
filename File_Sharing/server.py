import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))

server_socket.listen()
print("Server is listening")

client_socket, client_address = server_socket.accept()
print(f"connected to {client_address}")
data = client_socket.recv(1024).decode()
print("client messege: ", data)

client_socket.send("Hello from Server!".encode())

client_socket.close()
server_socket.close()