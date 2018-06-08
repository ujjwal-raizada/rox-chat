import socket
import threading
from threading import Thread
from queue import Queue
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


def ThreadCount():
    print("No. of active threads: "+str(threading.active_count()))

def server(conn, addr, id):
    print("connected:" + str(addr) + " id:"+ str(id))


    Ask = "Select your Username: "
    conn.send(Ask.encode())
    Username = conn.recv(1024).decode()
    userConfirm = "Username Registered!!"
    conn.send(userConfirm.encode())


    while True:
        data = conn.recv(1024).decode()
        if not data:
                break
        print ("from "+Username+": " + str(data))
        print ("Broadcasting: " + str(data))
        for con in conList:
            try:
                message = Username+": "+data
                con.send(message.encode())
            except:
                pass


             
    conn.close()
    print("Thread Died: "+str(id))




thread = []
conList = []
def Main():
    i = 0
    host = "127.0.0.1"
    port = 5006
     
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    

    while True:
        ThreadCount()
        mySocket.listen(1)
        conn, addr = mySocket.accept()
        print ("Connection from: " + str(addr))
        thread.append(Thread(target=server, args=(conn, addr, i)) )
        thread[i].deamon = True
        thread[i].start()
        print("thread_id: "+str(i)+" created")
        conList.append(conn)
        i+=1



if __name__ == '__main__':
    Main()
