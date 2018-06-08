import socket
from threading import Thread
import time


intro = """
██████╗  ██████╗ ██╗  ██╗ ██████╗██╗  ██╗ █████╗ ████████╗
██╔══██╗██╔═══██╗╚██╗██╔╝██╔════╝██║  ██║██╔══██╗╚══██╔══╝
██████╔╝██║   ██║ ╚███╔╝ ██║     ███████║███████║   ██║   
██╔══██╗██║   ██║ ██╔██╗ ██║     ██╔══██║██╔══██║   ██║   
██║  ██║╚██████╔╝██╔╝ ██╗╚██████╗██║  ██║██║  ██║   ██║   
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   

    """

print(intro)
host = '127.0.0.1'
port = 5004
 
mySocket = socket.socket()
mySocket.connect((host,port))


def MsgPrint():
    while True:
        data = mySocket.recv(1024).decode()
        if data:
            print ('Received from server: ' + data)
        else:
            break



 
def Main():

    thread = Thread(target=MsgPrint, args=(()))
    thread.deamon = True
    thread.start()

    print("Print thread created")
     
    message = input(" -> ")
     
    while message != 'q':
            mySocket.send(message.encode())
            message = input(" -> ")
             
    mySocket.close()
 
if __name__ == '__main__':
    Main()

