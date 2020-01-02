#client needs to run this script to connect to a server

import socket
import subprocess
import sys



 

#defining function for ssh connections
def ssh_connection(user_name="root"):
    print("Say the name of username:")
    user_name=voice_recognize()
    print("Say the ip:")
    ip_add=voice_recognize()
    print("Do you want to say the name and ip again")
    choice_for_y_n=voice_bool()
    if choice_for_y_n==1:
        ssh_connection()
    elif choice_for_y_n==0:
        os.system("ssh-keygen ; ssh-copy-id {}@{}".format(username,ip))
        return "Connected to {}@{}".format(username,ip),user_name,id_add     
    else:
        break


#STARTING THE MENU FROM HERE----------------------------------------//
os.system("tput setaf 1")
#Text to speeech used by the command festival
#os.system("echo welcome to world of linux|festival --tts")
print("\t\t\t\t\tWELCOME TO THE WORLD OF LINUX\n")
print("\n")
os.system("tput setaf 4")
#os.system("echo Where do you want to execute your command remote or local |festival --tts")
print("How do you want to work today? (remote/local):",end="")

#voice input from user
try:
    local=voice_location()
except:
    location=voice_location()
if location=='remote':
    user_name,ip_add=ssh_connection()
    s=socket.socket()
    print("Say the port number:")
    port=voice_recognize()
    #serverip=input("Give the server ip:")
    #serverport=int(input("Give the port number:"))
    #s.connect((serverip,serverport))
	s.connect((id_add,port))
    while True:
        print("""
            Option 1: Get Date
            Option 2: Get Cal
            Option 3: Open cheese
            Option 4: Take photo and save
            Option 5: Open Firefox 
            Option 6: Set Static Ip
            Option 7: Custom command
            Option 8: Install python3 and opencv
            Option 9: See the live stream
            Option 10: Add a user
            Option 11: To make a server
            """)
        print("Enter a choice :",end="")
        try:
            choice=choice()
        except:
            choice=choice()
#executing the choice commands  


elif location=="local":
	while True:    
    
























#calling function from different directory so added the sys module
sys.path.append("/home/crazypikachu/linux-based-project/Voice_based_commands")
from voice_recognize import voice_recognize
while True:
    cmd=input("Give me the command:")
    
    #command from voice_recognize file

    cmd=cmd.encode()
    s.send(cmd)
    if cmd == 'stop':
        break
    output_from_server=s.recv(2000)
    output_from_server=output_from_server.decode()
    print(output_from_server)




#function for remote or local connection
def voice_location():
    voice1=voice_recognize()
    if "remote" in voice1:
        return 'remote'
        break
    elif "local" in voice1:
        return 'local'
        break
    else :
        voice_location()

#fucntion for saying yes or no
def voice_bool():
    voice2=voice_recognize()
    if "no" in voice2 or "NO" in voice2 or "No" in voice2:
        return 0
        break
    elif "yes" in voice2 or "Yes" in voice2 or "YES" in voice2:    
        return 1
        break
    else:
        voice_bool()



#function for choice selection
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

