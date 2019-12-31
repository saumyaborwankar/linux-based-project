import socket
import subprocess
s=socket.socket()
serverip=input("Give the server ip:")
serverport=int(input("Give the port number:"))
s.connect((serverip,serverport))
print("Type 'stop' if you want to stop")
while True:
    cmd=input("Give me the command:")
    cmd=cmd.encode()
    s.send(cmd)
    if cmd == 'stop':
        break
    output_from_server=s.recv(2000)
    output_from_server=output_from_server.decode()
    print(output_from_server)
