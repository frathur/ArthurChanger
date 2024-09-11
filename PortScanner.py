#Building my port scanner
import termcolor
import subprocess
import socket 
#socket for communication over tcp and udp protocol

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect(ipaddress, port)
        print("[+] Port Opened ",str(port))
    except:
        print("[-] Port Closed", str(port))

#Scanning multiple ports
def scan(targets, ports):
    for port in range(1,ports):
        scan_port(targets, port)


targets = input("Enter targets to scan (Split multiple targets with ','): ")
ports = input("Enter number of ports you would like to scan: ")

if "," in targets:
    print("Scanning multiple targets ...")
    for target in targets.split(','):
        print(f"Scanning {targets.strip(' ')}")
        scan(targets.strip(' '), port)
else:
    print(f"Scanning {targets}")
    scan(targets, port)
