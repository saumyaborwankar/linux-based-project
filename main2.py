import os
import time

#clear the terminal
os.system("clear")

#declare the variables
Username=""
Ip=""
Stop="yes"

os.system("tput setaf 1")
#Text to speeech used by the command festival
#os.system("echo welcome to world of linux|festival --tts")
print("\t\t\t\t\tWELCOME TO THE WORLD OF LINUX\n")
print("\n")
os.system("tput setaf 4")
#os.system("echo Where do you want to execute your command remote or local |festival --tts")
print("How do you want to work today? (remote/local):",end="")
Location=input()

#using ssh-rsa to connect for once
if (Location=="remote"):
    print("Enter the remote IP :",end="")
    Ip=input()
    
    print("Username of remote :",end="")
    Username=input()
#    os.system("echo please leave all input feilds blank |festival --tts")
    print("Leave all the input feilds blank \n Establishing connection with {}@{}".format(Username,Ip))

    os.system("tput setaf 0")
#    os.system("ssh-keygen")
#copying ssh-keygen to remote host for bypassing password based authentication
    os.system("ssh-copy-id -i {}@{}".format(Username,Ip))

    os.system("tput setaf 7")
    print("connection established ")
    time.sleep(1)

#showing all the options 

os.system("tput setaf 2")
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


#executing the choice commands

while(Stop!="no"):
    print("Enter a choice :",end="")
    Numberchoice=int(input())
    os.system("tput setaf 6")
#choice number 1: to see date--------------------------------------------------------//
    if(Numberchoice==1):
        if(Location=="remote"):
            os.system("ssh {}@{} date".format(Username,Ip))
        else:
            os.system("date") 
#choice number 2: to see calendar---------------------------------------------------//
    elif(Numberchoice==2):
        if(Location=="remote"):
            os.system("ssh {}@{} cal".format(Username,Ip))
        else:
            os.system("cal")
#choice number 3: to open cheese----------------------------------------------------// 
    elif(Numberchoice==3):
        if(Location=="remote"):
            os.system("ssh -X {}@{} cheese".format(Username,Ip))
        else:
            os.system("cheese")
#choice number 4: to click a photo----------------------------------------------------//
    elif(Numberchoice==4):
        if(Location=="remote"):
            os.system("cat /capture_photo/photo.py | ssh {}@{} python3".format(Username,Ip))
            os.system("scp {}@{}:/tmp/photo.png ~/photo.png".format(Username,Ip))
        else:
            os.system("cat /capture_photo/photo.py | python3")
#choice number 5: to open firefox----------------------------------------------------//    
    elif(Numberchoice==5):
        print("Enter the name of website/Url to open :",end="")
        Website=input()
        if(Location=="remote"):
            os.system("ssh -X {}@{} firefox {}".format(Username,Ip,Website))
        else:
            os.system("firefox {}".format(Website))                      
#choice number 7: to use command----------------------------------------------------//
    elif(Numberchoice==7):
        print("enter the command :",end="")
        Command=input()
        if(Location=="remote"):
            os.system("ssh -X {}@{} {}".format(Username,Ip,Command))
        else:
            os.system("{}".format(Command))  
#choice number 6: to set static ip----------------------------------------------------//                                                
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
#choice number 8: to install python----------------------------------------------------//    
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
#choice number 9: to see the live stream----------------------------------------------------//    
    elif(Numberchoice==9):
        if(Location=="remote"):
            os.system("cat /home/crazypikachu/linux-based-project/video_capture.py | ssh {}@{} python3".format(Username,Ip))
            os.system("scp {}@{}:/tmp/photo.png ~/photo.png".format(Username,Ip))
        else:
            os.system("cat /home/crazypikachu/linux-based-project/video_capture.py | python3")
#choide number 10: to add a user--------------------------------------------------------------//
    elif(Numberchoice==10):
        print("Add the user name:", end="")
        u_name=input()
        print("Set the password:", end="")
        u_pwd=input()
        print("Do you want the user to be added to a group? (yes/no):", end="")
        u_grp=input()
        
        if(Location=="remote"):
            if u_grp=="yes":
                print("Type the group name")
                grp_name=input()
                os.system("ssh {}@{} groupadd {}",format(Username,Ip,grp_name))
                os.sytem("ssh {}@{} useradd -G {} {}".format(Username,Ip,grp_name,u_name))
                print("You'll need to enter the password on the terminal.")
                os.system("ssh {}@{} passwd {}".format(Username,Ip,u_name))
###############################################################   need to add password command  ########################################################
            elif u_grp=="no":
                os.system("ssh {}@{} useradd {}".format(Username,Ip,u_name))
            else:
                print("Please type 'yes' or 'no' and try again")
                
        else:
            os.system("useradd {}".format(u_name))                                    
#choice number 11: to make a server
    elif(Numberchoice==11):
        if (Location=="remote"):
            print("Starting the remote server")
            
#the server should run on the ip address as root???
            os.system("scp /home/crazypikachu/linux-based-project/Server\ programming/server.py {}@{}:/tmp/".format(Username,serv_ip))
#need to add the ip of the remote machine in the server.py file     ################################################################################
            os.system("ssh {}@{} cat > /tmp/server.py".format(Username,serv_ip))
            os.system()
            os.system("ssh {}@{} python3 /tmp/server.py".format(Username,serv_ip))
        elif (Location=="local"):
            print("Strating the local server")
            os.system("python3 /home/crazypikachu/linux-based-project/Server\ programming/server.py")

    else:
        print("Enter a valid choice ",end="")

    print("Do you want to use again :",end="")
    Stop=input()               
