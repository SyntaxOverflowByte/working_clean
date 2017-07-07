#!/usr/bin/python

'''
    A script to connect through the sockets module based on tcpClient and server
        Will first have to load the JSON file
        Will then make the user choose a VPS to connect
        Try to include argparse for specific information needed

'''

import json 
import os
import socket

INV_ROOT = os.path.join('/share/', 'inventory')
EGRESS_INV = os.path.join(INV_ROOT, 'egress_inventory.json')
KEYFILE = os.path.join(INV_ROOT, 'egress_keys/')


#Load JSON file
with open(EGRESS_INV) as f:
    egress_inventory = json.load(f)

#Iterate through names, make user choose, and return the choice
def egress_node():
    print "The VPS are as follows: "
    for count in range(len(egress_inventory)):
        egress_vps = egress_inventory[count]
        print "%d. %s : %s port:%d" % ( (count + 1), egress_vps['name'], egress_vps['location'], egress_vps['port'])
    user_choice = (int(raw_input("Please choose one: ")) - 1)
    chosen_vps = egress_inventory[user_choice]
    return(chosen_vps)

#Main function, connect to remote server
#Currently using the tcpClient.py as the base - 
#Will try to include a way to pass commands and return some information, 
#Possibly like a sys command?
def Main():
    VPS = egress_node()

    host = VPS['ip']
    port = VPS['port']

    #Create socket instance
    s = socket.socket()

    #Create the connection
    s.connect((host,port))

    #Do something while the connection is opened
    message = raw_input('-> ')
    while message != 'q':
        s.send(message)
        data = s.recv(1024)
        print ('Recieved from server: ' + str(data))
        message = raw_input('-> ')
    s.close()


if __name__ == '__main__':
    #Possibly a good place to put in argparse arguments
    Main()
