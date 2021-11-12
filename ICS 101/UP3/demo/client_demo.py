import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50002)) # need to know server port
"""
Send one message to SERVER
Receive one message back
"""
# send
msg = '--Hey Server--'
s.send(msg.encode('UTF-8'))

# receive
data = s.recv(1024)
print ('Received', repr(data))

"""
Continue chatting
"""
print('\n --chatting--- \n')
while True:
    # send
    msg = input('enter your message: ')
    s.send(msg.encode('UTF-8'))

    # receive
    data = s.recv(1024)
    print ('Server:', data.decode())

    # exit
    if msg == 'exit':
        data = s.recv(1024)
        print ('Received', data.decode())
        break

""" stop the connection """
s.close()
