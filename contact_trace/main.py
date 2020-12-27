import socket
import pickle
from contact_trace import form_information, tkinter_main, tkinterdash, tkinter_retrieve
    
#----------------------------------------------------------
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
#----------------------------------------------------------
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
#----------------------------------------------------------
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' *(HEADER-len(send_length)) 
    client.send(send_length)
    client.send(message)
    x = client.recv(2048).decode(FORMAT)
    return x
#----------------------------------------------------------
def step_1():
    tkinter_main.run()
    step_2()
#----------------------------------------------------------
def step_2():
    a = form_information.openloginfile()
    #print(a)
    x = send(a)
    if x != 'a':
        step_3(x)
    else:
        step_1()
#----------------------------------------------------------
def step_3(x):
    while True:
        tkinterdash.run()
        value = tkinterdash.key
        if value[0] == 'x':
            a = form_information.openfile()
            a = f'{str(x)}, ' + a
            print(a)
            cont = send(a)
            if cont:
                step_3(x)
        elif value[0] == 'y':
            b = form_information.open_multi()
            b = f'{str(x)}, ' + b
            print(b)
            cont = send(b)
            if cont:
                step_3(x)
        elif value[0] == 'z':
            c = str(x)
            if len(c) == 1:
                c += ', filler, filler, filler'
            print(c)
            cont = send(c)
            if cont != 'a':
                tkinter_retrieve.run(cont)
                print('Test loop', x)
                continue
            step_3(x)
        elif value[0] == 'w':
            d = str(x)
            if len(d) == 1:
                d += ', filler, filler, filler, filler'
            cont = send(d)
            if cont != 'a':
                tkinter_retrieve.run(cont)
                print('Test loop', x)
                continue
        else:
            print(value)           
#----------------------------------------------------------
step_1()
#send('!DISCONNECT')