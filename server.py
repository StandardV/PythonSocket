import socket
import os

#HOST = socket.gethostbyname(socket.gethostname())
HOST = '192.168.0.19'
PORT = 44132#9052
while(1):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    client, address = server.accept()
    #print(f"connected to {address}")
    while True:  
        if client.recv(1024).decode('utf-8') == 'sleep':
            break
    os.popen('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
