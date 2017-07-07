import socket

def Main():
    #Include a random choice for the port    
    host = '127.0.0.1'
    port = 2069
    print "Port: %d" % (port)
	
    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print('Connection from: ' + str(addr))
	
    while True:
	data = c.recv(1024)
	if not data:
		break
	print(' from connected user: ' + str(addr))
	data = str(data).upper()
	print('sending: ' + str(data))
	c.send(data)
	
	c.close()

if __name__ == '__main__':
	Main()
