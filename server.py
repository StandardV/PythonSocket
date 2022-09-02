import socket

#HOST = socket.gethostbyname(socket.gethostname())
HOST = '10.0.0.1' #this is the server and client HOST number should be based on it
PORT = 44132#9052

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
client, address = server.accept()
print(f"connected to {address}")
while True:  
    cmd_input = input("Enter a command: ")
    client.send(cmd_input.encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))



   
