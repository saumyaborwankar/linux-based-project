#client needs to run this script to connect to a server

import socket
import subprocess
import sys

s=socket.socket()

#serverip=input("Give the server ip:")
#serverport=int(input("Give the port number:"))
#s.connect((serverip,serverport))
s.connect(("192.168.43.183",1234))
print("Type 'stop' if you want to stop")
#calling function from different directory so added the sys module

sys.path.append("/home/crazypikachu/linux-based-project/Voice_based_commands")
from voice_recognize import voice_recognize
while True:
    cmd=input("Give me the command:")
    
    #command from voice_recognize file
    def choice()
        voice=voice_recognize()
        print(voice)
        if "date" in voice and "get" in voice:
            return 1
        elif "calendar" in voice and "get" in voice:
            return 2    
        elif "open" in voice and "cheese" in voice:
            return 3
        elif "photo" in voice and "save" in voice:
            return 4
        elif "open" in voice and "Firefox" in voice:
            return 5
        elif "set" in voice and "static" in voice:
            return 6
        elif "custom" in voice and "command" in voice:
            return 7
        elif "install" in voice and "python" in voice:
            return 8                     
        else:
            return 0
    cmd=cmd.encode()
    s.send(cmd)
    if cmd == 'stop':
        break
    output_from_server=s.recv(2000)
    output_from_server=output_from_server.decode()
    print(output_from_server)





def voice_location():
    voice1=voice_recognize()
    if "remote" in voice1:
        return 1
        break
    elif "local" in voice1:
        return 0
        break
    else :
        voice_location()

def 