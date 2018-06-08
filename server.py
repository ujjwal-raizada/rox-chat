import socket
import threading
from threading import Thread
from queue import Queue
import time


q = Queue()


def ThreadCount():
    print(threading.active_count())

def server(conn, addr, id):
    print("connected:" + str(addr) + "id:"+ str(id))

    while True:
        data = conn.recv(1024).decode()
        if not data:
                break
        print ("from connected  user: " + str(data))
         
        data = str(data).upper()
        print ("sending: " + str(data))
        for c in tconn:
            c.send(data.encode())

             
    conn.close()
    print("Thread Died: "+str(id))




thread = []
tconn = [] 
def Main():
    i = 0
    host = "127.0.0.1"
    port = 5004
     
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    

    while True:
        ThreadCount()
        mySocket.listen(1)
        conn, addr = mySocket.accept()
        print ("Connection from: " + str(addr))
        thread.append(Thread(target=server, args=(conn, addr, i)) )
        thread[i].start()
        print("thread: "+str(i)+" created")
        tconn.append(conn)
        print("tcon: "+str(tconn))
        i+=1





if __name__ == '__main__':
    Main()
