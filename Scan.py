import socket, subprocess, termcolor

def scan(target, ports):
    for port in range(1, ports):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        status = sock.connect_ex()
        if status == "0"
