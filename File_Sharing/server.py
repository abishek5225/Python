import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))

server_socket.listen()
print("Server is listening")

client_socket, client_address = server_socket.accept()
print(f"connected to {client_address}")

filename = client_socket.recv(1024).decode()
print(f"Receiving file: {filename}")

with open("received_"+ filename, "wb") as f:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        f.write(data)
print("File received successfully!")
client_socket.close()
server_socket.close()