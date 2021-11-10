import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50002)) # need to know server port
# user control the connection
s.send(b'I want to chat?')
data = s.recv(1024)
print(data.decode('UTF-8'))
print('--chatting--- \n')
while True:
    msg = input('enter your response: ')
    s.send(msg.encode('UTF-8'))
    data = s.recv(1024)
    print ('Received')
    print(data.decode('UTF-8'))
    if msg == 'exit':
        data = s.recv(1024)
        print ('Received')
        print(data.decode('UTF-8'))
        break

s.close()
