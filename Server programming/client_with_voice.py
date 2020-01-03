#client needs to run this script to connect to a server

import socket
import subprocess
import sys
import os
#calling function from different directory so added the sys module
sys.path.append("/home/crazypikachu/linux-based-project/Voice_based_commands")
from voice_recognize import voice_recognize
"""while True:
    cmd=input("Give me the command:")
    
    #command from voice_recognize file

    cmd=cmd.encode()
    s.send(cmd)
    if cmd == 'stop':
        break
    output_from_server=s.recv(2000)
    output_from_server=output_from_server.decode()
    print(output_from_server)
"""



#function for remote or local connection
def voice_location():
    voice1=voice_recognize()
    if "remote" in voice1:
        return 'remote'
        
    elif "local" in voice1:
        return 'local'
        
    else :
        voice_location()

#fucntion for saying yes or no
def voice_bool():
    voice2=voice_recognize()
    if "no" in voice2 or "NO" in voice2 or "No" in voice2:
        return 0
    elif "yes" in voice2 or "Yes" in voice2 or "YES" in voice2:    
        return 1
    else:
        voice_bool()



#function for choice selection
def choice():
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
        os.system("ssh-keygen ; ssh-copy-id {}@{}".format(user_name,ip_add))
        return user_name,ip_add     
    


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
    location=voice_location()
except:
    location=voice_location()
print(location)
if location=="remote":
    user_name,ip_add=ssh_connection()
    s=socket.socket()
    print("Say the port number:")
    port=voice_recognize()
    port=int(port)
    #serverip=input("Give the server ip:")
    #serverport=int(input("Give the port number:"))
    #s.connect((serverip,serverport))

    s.connect( (ip_add,port) )
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

        if(choice==1):
            if(location=="remote"):
                os.system("ssh {}@{} date".format(Username,Ip))
            else:
                os.system("date") 
#choice number 2: to see calendar---------------------------------------------------//
        elif(choice==2):
            if(location=="remote"):
                os.system("ssh {}@{} cal".format(Username,Ip))
            else:
                os.system("cal")
#choice number 3: to open cheese----------------------------------------------------// 
        elif(choice==3):
            if(location=="remote"):
                os.system("ssh -X {}@{} cheese".format(Username,Ip))
            else:
                os.system("cheese")
#choice number 4: to click a photo----------------------------------------------------//
        elif(choice==4):
            if(location=="remote"):
                os.system("cat /capture_photo/photo.py | ssh {}@{} python3".format(Username,Ip))
                os.system("scp {}@{}:/tmp/photo.png ~/photo.png".format(Username,Ip))
            else:
                os.system("cat /capture_photo/photo.py | python3")
    #choice number 5: to open firefox----------------------------------------------------//    
        elif(choice==5):
            print("Enter the name of website/Url to open :",end="")
            Website=input()
            if(location=="remote"):
                os.system("ssh -X {}@{} firefox {}".format(Username,Ip,Website))
            else:
                os.system("firefox {}".format(Website))                      
    #choice number 7: to use command----------------------------------------------------//
        elif(choice==7):
            print("enter the command :",end="")
            Command=input()
            if(location=="remote"):
                os.system("ssh -X {}@{} {}".format(Username,Ip,Command))
            else:
                os.system("{}".format(Command))  
    #choice number 6: to set static ip----------------------------------------------------//                                                
        elif(choice==6):
            if(location=="remote"):
                print("""Enter connection name \nEnter Ip with netmask \nEnter interface name \nEnter gateway \nEnter interface type \nEnter new Dns server""")
                StaticName=input()	
                StaticIp=input()
                StaticInterfaceName=input()
                StaticGateway=input()
                StaticInterfacetype=input()
                StaticDns=input()	
            if(location=="remote"):

                os.system("ssh  {}@{} nmcli connection add con-name {} ifname {} type {} ip4 {} gw4 {}".format(Username,Ip,StaticName,StaticInterfaceName,StaticInterfacetype,StaticIp,StaticGateway))
                os.system("ssh {}@{} nmcli connection mod {} ipv4.dns {}".format(Username,Ip,StaticName,StaticDns))
            else:
                os.system("nmcli connection add con-name {} ifname {} type {} ip4 {} gw4 {}".format(Username,Ip,StaticName,StaticInterfaceName,StaticInterfacetype,StaticIp,StaticGateway))
                os.system("nmcli connection mod {} ipv4.dns {}".format(Username,Ip,StaticName,StaticDns)) 
    #choice number 8: to install python----------------------------------------------------//    
        elif(choice==8):
            if(location=="remote"):
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
        elif(choice==9):
            if(location=="remote"):
                os.system("cat /home/crazypikachu/linux-based-project/video_capture.py | ssh {}@{} python3".format(Username,Ip))
                os.system("scp {}@{}:/tmp/photo.png ~/photo.png".format(Username,Ip))
            else:
                os.system("cat /home/crazypikachu/linux-based-project/video_capture.py | python3")
    #choide number 10: to add a user--------------------------------------------------------------//
        elif(choice==10):
            print("Add the user name:", end="")
            u_name=input()
            print("Set the password:", end="")
            u_pwd=input()
            print("Do you want the user to be added to a group? (yes/no):", end="")
            u_grp=input()
            
            if(location=="remote"):
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
        elif(choice==11):
            if (location=="remote"):
                print("Starting the remote server")
                
    #the server should run on the ip address as root???
                os.system("scp /home/crazypikachu/linux-based-project/Server\ programming/server.py {}@{}:/tmp/".format(Username,serv_ip))
    #need to add the ip of the remote machine in the server.py file     ################################################################################
                os.system("ssh {}@{} cat > /tmp/server.py".format(Username,serv_ip))
                os.system()
                os.system("ssh {}@{} python3 /tmp/server.py".format(Username,serv_ip))
            elif (location=="local"):
                print("Strating the local server")
                os.system("python3 /home/crazypikachu/linux-based-project/Server\ programming/server.py")
        print("Do you want to use again :")    
        if(voice_bool()==0):
            break
elif location=="local":
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
        if(choice==1):
            if(location=="remote"):
                os.system("ssh {}@{} date".format(Username,Ip))
            else:
                os.system("date") 
#choice number 2: to see calendar---------------------------------------------------//
        elif(choice==2):
            if(location=="remote"):
                os.system("ssh {}@{} cal".format(Username,Ip))
            else:
                os.system("cal")
#choice number 3: to open cheese----------------------------------------------------// 
        elif(choice==3):
            if(location=="remote"):
                os.system("ssh -X {}@{} cheese".format(Username,Ip))
            else:
                os.system("cheese")
#choice number 4: to click a photo----------------------------------------------------//
        elif(choice==4):
            if(location=="remote"):
                os.system("cat /capture_photo/photo.py | ssh {}@{} python3".format(Username,Ip))
                os.system("scp {}@{}:/tmp/photo.png ~/photo.png".format(Username,Ip))
            else:
                os.system("cat /capture_photo/photo.py | python3")
    #choice number 5: to open firefox----------------------------------------------------//    
        elif(choice==5):
            print("Enter the name of website/Url to open :",end="")
            Website=input()
            if(location=="remote"):
                os.system("ssh -X {}@{} firefox {}".format(Username,Ip,Website))
            else:
                os.system("firefox {}".format(Website))                      
    #choice number 7: to use command----------------------------------------------------//
        elif(choice==7):
            print("enter the command :",end="")
            Command=input()
            if(location=="remote"):
                os.system("ssh -X {}@{} {}".format(Username,Ip,Command))
            else:
                os.system("{}".format(Command))  
    #choice number 6: to set static ip----------------------------------------------------//                                                
        elif(choice==6):
            if(location=="remote"):
                print("""Enter connection name \nEnter Ip with netmask \nEnter interface name \nEnter gateway \nEnter interface type \nEnter new Dns server""")
                StaticName=input()	
                StaticIp=input()
                StaticInterfaceName=input()
                StaticGateway=input()
                StaticInterfacetype=input()
                StaticDns=input()	
            if(location=="remote"):

                os.system("ssh  {}@{} nmcli connection add con-name {} ifname {} type {} ip4 {} gw4 {}".format(Username,Ip,StaticName,StaticInterfaceName,StaticInterfacetype,StaticIp,StaticGateway))
                os.system("ssh {}@{} nmcli connection mod {} ipv4.dns {}".format(Username,Ip,StaticName,StaticDns))
            else:
                os.system("nmcli connection add con-name {} ifname {} type {} ip4 {} gw4 {}".format(Username,Ip,StaticName,StaticInterfaceName,StaticInterfacetype,StaticIp,StaticGateway))
                os.system("nmcli connection mod {} ipv4.dns {}".format(Username,Ip,StaticName,StaticDns)) 
    #choice number 8: to install python----------------------------------------------------//    
        elif(choice==8):
            if(location=="remote"):
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
        elif(choice==9):
            if(location=="remote"):
                os.system("cat /home/crazypikachu/linux-based-project/video_capture.py | ssh {}@{} python3".format(Username,Ip))
                os.system("scp {}@{}:/tmp/photo.png ~/photo.png".format(Username,Ip))
            else:
                os.system("cat /home/crazypikachu/linux-based-project/video_capture.py | python3")
    #choide number 10: to add a user--------------------------------------------------------------//
        elif(choice==10):
            print("Add the user name:", end="")
            u_name=input()
            print("Set the password:", end="")
            u_pwd=input()
            print("Do you want the user to be added to a group? (yes/no):", end="")
            u_grp=input()
            
            if(location=="remote"):
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
        elif(choice==11):
            if (location=="remote"):
                print("Starting the remote server")
                
    #the server should run on the ip address as root???
                os.system("scp /home/crazypikachu/linux-based-project/Server\ programming/server.py {}@{}:/tmp/".format(Username,serv_ip))
    #need to add the ip of the remote machine in the server.py file     ################################################################################
                os.system("ssh {}@{} cat > /tmp/server.py".format(Username,serv_ip))
                os.system()
                os.system("ssh {}@{} python3 /tmp/server.py".format(Username,serv_ip))
            elif (location=="local"):
                print("Strating the local server")
                os.system("python3 /home/crazypikachu/linux-based-project/Server\ programming/server.py")
        print("Do you want to use again :")    
        if(voice_bool()==0):
            break   