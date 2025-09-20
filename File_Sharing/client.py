import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))


filename= "testfile.txt"
client_socket.send(filename.encode())

#acknowledgement
ack = client_socket.recv(1024).decode()
print("Server: ", ack)

with open(filename, "rb") as f:
    data= f.read(1024)
    while data:
        client_socket.send(data)
        data=f.read(1024)



print("file sent successfully")

client_socket.close()