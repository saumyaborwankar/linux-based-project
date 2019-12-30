import os
os.system("echo welcome to this tool | festival --tts")
os.system("tput setaf 1")
print("\t\t\tWelcome to this tool")
os.system("tput setaf 3")
print("\t\t\t....................")
print("")
i=1

print("How do you wish to work today? (remote/local)", end="")
loc=input()
if loc=='remote':
	print("Please tell us the ip of the remote server:")
	os.system("ssh-keygen")
	print("Username:",end="")
	username=input()
	print("IP:",end="")
	loc_ip=input()

	os.system("ssh-copy-id -i {}@{}".format(username,loc_ip))
	os.system("ssh-add")

	while 1:
		os.system("tput setaf 4")
		print("Press 1: to show the date")
		print("Press 2: to show the cal")
		print("Press 3: to create a folder")
		print("Press 4: to create a file")
		print("Press 5: to install a package ")
		print("Press 6: to click a photo")
		print("Press 7: to exit ")
		choice=input()
		choice=int(choice)
		if choice == 1:
			os.system("ssh {}@{} date".format(username,loc_ip))
		elif choice == 2:
			os.system("ssh {}@{} cal".format(username,loc_ip))
		elif choice == 3:
			print("Please enter the name of the folder you'd like to create:",end="")
			folder_name=input
			os.system("ssh {} mkdir {}".format(loc_ip, folder_name))
		elif choice == 4:
			print("Please enter the name of the file you'd like to create:",end="")
			file_name=input
			os.system("ssh {} touch {}".format(loc_ip, file_name))
		elif choice == 5:
			print("Please enter the name of the package you'd like to install:",end="")
			package_name=input
			os.system("ssh {}@{} yum install {}".format(username,loc_ip, package_name))
		elif choice == 6:
			os.system("scp /root/Desktop/package.tar.gz {}@{}:~/".format(username,loc_ip))
			os.system("ssh {}@{} tar -xf ~/package.tar.gz".format(username,loc_ip))
			os.system("ssh {}@{} yum install ~/package/python36-pip-8.1.2-8.el7.noarch.rpm".format(username,loc_ip))
			os.system("ssh {}@{} pip3 install ~/opencv_python-4.0.0.21-cp36-cp36m-manylinux1_x86_64.whl --no-index -f ~/".format(username,loc_ip))
			os.system("ssh {}@{} 


			os.system("scp /root/Desktop/lw_project/click_photo.py {}@{}:~/".format(username,loc_ip))			
			os.system("ssh {}@{} python3 click_photo.py".format(username,loc_ip))
			os.system("scp {}@{}:~/photo.jpeg /root/Desktop/lw_project".format(username,loc_ip))	
		elif choice == 7:
			break
		else:
			print("Please enter valid number")
elif loc=='local':
	print("You're working in this local machine")
	print("")
	while 1:	
		print("Press 1: to show the date")
		print("Press 2: to show the cal")
		print("Press 3: to create a folder")
		print("Press 4: to create a file")
		print("Press 5: to install a package ")
		print("Press 6: to quit")
		choice=input()
		choice=int(choice)
		if choice == 1:
			os.system("date")
		elif choice == 2:
			os.system("cal")
		elif choice == 3:
			print("Please enter the name of the folder you'd like to create:",end="")
			folder_name=input
			os.system("mkdir {}".format( folder_name))
		elif choice == 4:
			print("Please enter the name of the file you'd like to create:",end="")
			file_name=input
			os.system("touch {}".format(file_name))
		elif choice == 5:
			print("Please enter the name of the package you'd like to install:",end="")
			package_name=input
			os.system("yum install {}".format(loc_ip, package_name))
		elif choice == 6:
			break	
		else:
			print("Please enter a valid number")
else:
	print("Please enter \"remote\" or \"local\" as an option and try again")
os.system("tput setaf 0")
	 

