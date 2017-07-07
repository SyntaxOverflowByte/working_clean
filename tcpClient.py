import socket

def Main():
	host = '127.0.0.1'
	port = 5000
	
	#Create the socket instance
	s = socket.socket()
	
	#create the connection
	s.connect((host,port))
	
	#Do something while the connection is opened
	message = raw_input('-> ')
	while message != 'q':
		s.send(message)
		data = s.recv(1024)
		print('Recieved from server: ' + str(data))
		message = raw_input('-> ')
	s.close()


if __name__ == '__main__':
	Main()
