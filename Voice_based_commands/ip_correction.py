#resolving errors in ip (spaces and dots)
#integrate it with voice_recognize.py
import numpy as np
print("Say the ip address without the 'dots'")
voice=input()
list1=list(voice)
for i in range(len(voice)):
    if list1[i]==' ' and list1[i+1]=='d':
        list1[i]='.'
        list1[i+1]=''
        list1[i+2]=''
        list1[i+3]=''
        list1[i+4]=''
        voice = ''.join(list1)
    if list1[i]==' ':
        list1[i]='.'
        voice=''.join(list1)    
print(voice)
