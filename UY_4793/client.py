import socket

HOST = "127.0.0.1" 
PORT = 1112 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #TCP
#with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: #UDP
    s.connect((HOST, PORT)) #connect to port
    while True:
        s.sendall(input("Ask your question:").encode()) #encode to bits and send
        data = str(s.recv(1024), encoding='utf-8') #decodes at most 1024 bytes
        
        print(f"Bot: {data}")
        if data == "bye": #bye ends loop
            break