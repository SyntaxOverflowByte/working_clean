import socket
import json
import os
import random

INV_ROOT = os.path.join('/share/', 'inventory')
EGRESS_INV = os.path.join(INV_ROOT, 'egress_inventory.json')

def port_return():
    egress_ports = []
    with open(EGRESS_INV) as f:
        egress_inventory = json.load(f)
    for count in range(len(egress_inventory)):
        egress_ports.append(egress_inventory[count]['port'])
    return egress_ports


def Main():
    #Include a random choice for the port
    vps_ports = port_return()
    port = random.choice(vps_ports)
    host = '127.0.0.1'
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
