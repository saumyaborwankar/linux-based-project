#making a local server using python

import socket
import subprocess
s=socket.socket()

#setting permanent port

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADD,1)
ip="192.168.43.183"
port=1234
s.bind((ip,port))
clsession=[0]
clip=[0]
i=0
print("Type 'stop' to stop")
while True:
    s.listen()
    clsession[i],clip[i]=s.accept()
    data =clsession[0].recv(100)
    cmd=data.decode()
    if cmd=='stop':
        break
    output=subprocess.getoutput(cmd)
    output=output.encode()
    clsession[0].send(output)
    i=i+1
    print(output)
    