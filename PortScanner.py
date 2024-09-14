#Building my port scanner
import termcolor
import subprocess
import socket 
#socket for communication over tcp and udp protocol
subprocess.call(['figlet', 'ArtScan',])
def scan_port(ipaddress, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            status = sock.connect_ex((ipaddress, port))
            if status == 0:
                print(termcolor.colored((f"[+] Port Opened {str(port)}") , 'green'))
            else:
                pass
            sock.close()
        except:
            pass
            sock.close()
                

#Scanning multiple ports
def scan(target, ports):
    for port in range(1,ports):
        scan_port(target, port)


targets = input("Enter targets to scan (Split multiple targets with ','): ")
ports =int( input("Enter number of ports you would like to scan: "))

if "," in targets:
    print(termcolor.colored(("Scanning multiple targets ..."),'blue'))
    for target in targets.split(','):
        print(f"Scanning {targets.strip(' ')}")
        scan(targets.strip(' '), ports)
else:
    print(termcolor.colored((f"Scanning {targets}"), 'blue'))
    scan(targets, ports)
