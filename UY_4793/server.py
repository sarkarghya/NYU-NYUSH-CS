import socket
from time import sleep
import string

HOST = "127.0.0.1"  # localhost
PORT = 1112  # non privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #TCP (reliable)
#with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: #UDP (un reliable)
    s.bind((HOST, PORT)) #binds port
    s.listen(5) #how many non-accepted connections are allowed to be outstanding.
    conn, add = s.accept() #host and port
    with conn:
        print(f"Now connected to {add}")
        while True: #server loop
            raw_data = str(conn.recv(1024), encoding='utf-8') #decodes at most 1024 bytes
            ## some basic manipulation before matching questions
            data = ''.join(ch for ch in raw_data if ch not in set(string.punctuation))
            if data.lower() == "bye": #bye ends loop
                conn.sendall(data.encode())
                break #socket closed at end of loop
            elif data.lower() == "who are you":
                mess = "I am a bot!"
            elif data.lower() == "do you like me":
                mess = "I like you very much <3"
            elif data.lower() == "howdy":
                mess = "Just fine pal!"
            else:
                mess = "Hey why not type something else!"
            conn.sendall(mess.encode()) #encode to bits and send
            sleep(2) #sleep to not burden cpu