import socket
import subprocess 
import time
import os
import pyaudio
import speech_recognition as str
from speech import speech_execution
from speech import speech_bool
from speech import speech

ip="192.168.43.161"
port=1234


def ssh_connect(username="root"):
    print("Please leave options blank for easy configuation !")
    os.system("ssh-keygen ; ssh-copy-id {}@{}".format(username,ip))
    return "Connected to {}@{}".format(username,ip)

#def term(cmd):
 #   output=subprocess.getoutput(cmd)
  #  return output

def decode_choice(choice,username):
    if(choice==1):
        message="date"
    elif(choice==2):
        message="cal"
    elif(choice==6):
        print("""Enter connection name \nEnter Ip with netmask \nEnter interface name \nEnter gateway \nEnter interface type \nEnter new Dns server""")
        StaticName=input()
        StaticIp=input()
        StaticInterfaceName=input()
        StaticGateway=input()
        StaticInterfacetype=input()
        StaticDns=input()        
        os.system("ssh  {}@{} nmcli connection add con-name {} ifname {} type {} ip4 {} gw4 {}".format(username,ip,StaticName,StaticInterfaceName,StaticInterfacetype,StaticIp,StaticGateway))
        os.system("ssh {}@{} nmcli connection mod {} ipv4.dns {}".format(username,ip,StaticName,StaticDns))        
    elif(choice==7):
        message=input("Enter your command :")
    elif(choice==8):
        if(input("Enter your system type (debian/redhat) :")=="debian"):
            message="apt-get install python3.6 ;apt-get install python3-opencv"
        else:
            message="yum install python36 ;yum install python36-opencv"
    else:
        message="clear"
        print("enter a valid choice")
    
    return(message)

def graphical_execution(choice,username):
    if choice==3:
        os.system("cat /home/home/pythoncodes/swiss-army-knife-of-linux/udp-file/vedio.py | ssh -X {}@{} python3".format(username,ip))
    elif choice==4: 
        os.system("cat photo.py | ssh {}@{} python3".format(username,ip))
        os.system("scp {}@{}:~/photo.png ~/photo1.png".format(username,ip)) 
        
    elif choice==5:
        os.system("ssh -X {}@{} firefox".format(username,ip))    
        

os.system("tput setaf 1")
print("\t\t\t\tWelcome to world of automated linux")
print("Where do you want to execute your command (remote/local) :")
os.system("tput setaf 3")

try:
    location=speech_execution()
except:
    location=speech_execution()    

if(location=="remote"):
    username=input("Enter remote username :")
    s=socket.socket()

    
    while True:

        print("""
            Option 1: Get Date
            Option 2: Get Cal
            Option 3: Open cheese and take photo
            Option 4: Take photo and save
            Option 5: Open Firefox 
            Option 6: Set Static Ip
            Option 7: Custom command
            Option 8: Install python3 and opencv
        """)
        message="cd ."
        #int(input("Enter the choice :"))
        print("enter your choice :")
        try:
            choice=speech()
        except:
            choice=speech()    
        print(choice)
        if(choice==3 or choice==4 or choice==5):
            
            print(ssh_connect(username))
            graphical_execution(choice,username)
            clientsock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            clientsock.sendto(message.encode(),(ip,port))
            time.sleep(1)               
        else:        
            message=decode_choice(choice,username)
            clientsock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            clientsock.sendto(message.encode(),(ip,port))
            time.sleep(1)
            data,addr=clientsock.recvfrom(1024)
            print(addr)
            print(data.decode())
        os.system("tput setaf 1")    
        print("Do you want to use again :")    
        if(speech_bool()==1):
            break
