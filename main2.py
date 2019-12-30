import os
import time

#clear the terminal
os.system("clear")

#declare the variables
Username=""
Ip=""
Stop="yes"

os.system("tput setaf 1")
os.system("echo welcome to world of linux|festival --tts")
print("\t\t\t\t\tWELCOME TO THE WORLD OF AUTMATED LINUX\n")
print("\n")
os.system("tput setaf 4")
os.system("echo Where do you want to execute your command remote or local |festival --tts")
print("Where do you want to execute your command (remote/local):",end="")
Location=input()

#using ssh-rsa to connect for once
if (Location=="remote"):
    print("enter the remote IP :",end="")
    Ip=input()
    
    print("username of remote :",end="")
    Username=input()
    os.system("echo please leave all input feilds blank |festival --tts")
    print("leave all the input feilds blank \n Establishing connection with {}@{}".format(Username,Ip))

    os.system("tput setaf 0")
    os.system("ssh-keygen")
    os.system("ssh-copy-id -i {}@{}".format(Username,Ip))

    os.system("tput setaf 7")
    print("connection established ")
    time.sleep(1)

#showing all the options 

os.system("tput setaf 2")
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


#executing the choice commands

while(Stop!="no"):
    print("Enter a choice :",end="")
    Numberchoice=int(input())
    os.system("tput setaf 6")
    if(Numberchoice==1):
        if(Location=="remote"):
            os.system("ssh {}@{} date".format(Username,Ip))
        else:
            os.system("date") 
    elif(Numberchoice==2):
        if(Location=="remote"):
            os.system("ssh {}@{} cal".format(Username,Ip))
        else:
            os.system("cal")
    elif(Numberchoice==3):
        if(Location=="remote"):
            os.system("ssh -X {}@{} cheese".format(Username,Ip))
        else:
            os.system("cheese")
    elif(Numberchoice==4):
        if(Location=="remote"):
            os.system("cat photo.py | ssh {}@{} python3".format(Username,Ip))
            os.system("scp {}@{}:~/photo.png ~/photo.png".format(Username,Ip))
        else:
            os.system("cat photo.py | python3")
    elif(Numberchoice==5):
        print("Enter the name of website/Url to open :",end="")
        Website=input()
        if(Location=="remote"):
            os.system("ssh -X {}@{} firefox {}".format(Username,Ip,Website))
        else:
            os.system("firefox {}".format(Website))                      
    elif(Numberchoice==7):
        print("enter the command :",end="")
        Command=input()
        if(Location=="remote"):
            os.system("ssh -X {}@{} {}".format(Username,Ip,Command))
        else:
            os.system("{}".format(Command))                                      
    elif(Numberchoice==6):
        if(Location=="remote"):
	        print("""Enter connection name \nEnter Ip with netmask \nEnter interface name \nEnter gateway \nEnter interface type \nEnter new Dns server""")
	        StaticName=input()	
	        StaticIp=input()
	        StaticInterfaceName=input()
	        StaticGateway=input()
	        StaticInterfacetype=input()
	        StaticDns=input()	
        if(Location=="remote"):

            os.system("ssh  {}@{} nmcli connection add con-name {} ifname {} type {} ip4 {} gw4 {}".format(Username,Ip,StaticName,StaticInterfaceName,StaticInterfacetype,StaticIp,StaticGateway))
            os.system("ssh {}@{} nmcli connection mod {} ipv4.dns {}".format(Username,Ip,StaticName,StaticDns))
        else:
            os.system("nmcli connection add con-name {} ifname {} type {} ip4 {} gw4 {}".format(Username,Ip,StaticName,StaticInterfaceName,StaticInterfacetype,StaticIp,StaticGateway))
            os.system("nmcli connection mod {} ipv4.dns {}".format(Username,Ip,StaticName,StaticDns)) 
    elif(Numberchoice==8):
        if(Location=="remote"):
            print("please enter type of os (debian/redhat) :",end="")
            Systemtype=input()
            if(Systemtype=="debian"):
                os.system("ssh {}@{} apt-get install python3.6".format(Username,Ip))
                os.system("ssh {}@{} apt-get install python3-opencv".format(Username,Ip))
                print("installation compelete")
            else:
                os.system("scp /home/home/pythoncodes/swiss-army-knife-of-linux/packages.tar.xz {}@{}:~/".format(Username,Ip))
                os.system("ssh {}@{} tar -xf /root/packages.tar.xz".format(Username,Ip))
                os.system("ssh {}@{} yum install /root/python36-3.6.6-5.el7.x86_64.rpm python36-pip-8.1.2-8.el7.noarch.rpm".format(Username,Ip))
                os.system("ssh {}@{} pip3 install opencv_python-4.0.0.21-cp36-cp36m-manylinux1_x86_64.whl --no-index -f /root/".format(Username,Ip))
                print("installation compelete")

    else:
        print("Enter a valid choice ",end="")

    print("do you want to use again :",end="")
    Stop=input()               
