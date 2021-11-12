# https://pymotw.com/2/select/

import socket, select
import utils
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 50002))
# if use s.bind(s.gethostname(), 50002) , server would be visiable to outside world
# if use s.bind('localhost, 50002), server is only visiable within the same machine """
# if address already in use: ps -fA | grep python or sudo lsof -i:8080

server.listen(5)
# queue up as many as 5 connection requestion.
all_sockets = [server]
all_clients = {}

# create a new socket "conn", and also return the client address
# only serving one incoming connection
print('starting server')
count = 1
while 1:
    print('---round {} -----'.format(count))
    print()
    read, write, error = select.select(all_sockets, [], [])
    # readable sockets: have incoming data in buffer, ready to be read
    # writable sockets: have free space in their buffer, can be written to
    #print(read, write, error)
    for r in read:
        if r is server:
            (conn, addr) = r.accept()
            print('Got connection from', addr)

            # reads data from the socket in batches of 1024 bytes.
            msg = conn.recv(1024)
            print(msg)
            conn.send(b'Welcome \n Please type in your username or "exit" to stop:')
            data = conn.recv(1024)
            msg = data.decode('UTF-8')

            if msg == 'exit':
                conn.send(b'\n bye ~ ~')
                break # close the connection
            else:
                all_sockets.append(conn)
                all_clients[msg] = conn
                print( msg + ' joined ')
                conn.send(b'\n options: xxxxx')
        else:
            data = r.recv(1024)
            # reads data from the socket in batches of 1024 bytes.
            print(data.decode('UTF-8'))
            r.send(b'got you!' + data)
            if data.decode('UTF-8') == 'exit':
                r.send(b'\n bye ~ ~')
                r.close()
                all_sockets.remove(r) # close the connection

        count += 1
