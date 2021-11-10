import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""start the socket at a particular port"""
s.bind(('localhost', 50002))
"""
# if use s.bind(s.gethostname(), 50002) , server would be visiable to outside world
# if use s.bind('localhost, 50002), server is only visiable within the same machine
# if address already in use: ps -fA | grep python or sudo lsof -i:8080
"""
s.listen(5) # queue up as many as 5 connection request.
print('\n -----server ready------')
"""
# create a new socket "conn", and also return the client address
# now only serving one incoming connection
"""
(conn, addr) = s.accept()
print('Got connection from', addr)

"""
Receive one message from Client
Send one message back
"""
# receive
data = conn.recv(1024)
print (data.decode())

# send
conn.send('you said: '.encode('UTF-8') + data)
"""
Continue chatting
"""
while 1:
    # receive
    data = conn.recv(1024) # reads data from the socket in batches of 1024 bytes.
    print(data.decode())

    # send
    conn.send('you said: '.encode('UTF-8') + data)

    # handle exit request
    if data.decode('UTF-8') == 'exit':
        conn.send(b'bye ~ ~')
        break # close the connection
s.close()
