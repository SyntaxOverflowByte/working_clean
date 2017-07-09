#!/usr/bin/python
'''
    Initial attempt to iterate through the JSON file
'''

import JSON
import simplejson
import os
from Crypto.PublicKey import RSA
import socket

INV_ROOT = os.path.join('/share/', 'inventory/')
EGRESS_INV = os.path.join(INV_ROOT, 'egress_inventory.json')
KEYFILE = os.path.join(INV_ROOT, 'egress_keys/')
FWD_INV = os.path.join(INV_ROOT, 'inventory.json')

#Load JSON file into memory
with open(EGRESS_INV) as f:
    egress_inventory = json.load(f)

#Iterate through only the names
'''
#Iterate method 1 - Not as good to interate through
for item in egress_inventory():
    for attribute, value in item.iteritems():
        if attribute == str('name'):
            print value
'''
#Iterate method 2 - seems to be a better way

for count in range(len(egress_inventory)):
    egress_vps = egress_inventory[count]
    print "The VPS are as follows: %s : %s" % (egress_vps['name'], egress_vps['ip'])
#    print egress_inventory[count]['name']
#    print egress_inventory[count][

# List and choose a VPS to connect through
def egress_node():
    print "The VPS are as follows: "
    for count in range(len(egress_inventory)):
        egress_vps = egress_inventory[count]
        print "%d %s : %s" % ( (count + 1), egress_vps['name'], egress_vps['location'])
    user_choice = (int(raw_input("Please choose one: ")) - 1)
    chosen_vps = egress_inventory[user_choice]
    print "Your choice is: %s at IP %s out of %s" % (chosen_vps['name'], chosen_vps['ip'], chosen_vps['location'])
    return(chosen_vps)

#Create variable (VPS) to use specific VPS - now only need VPS[key] for value

VPS = egress_node()

#Generate public and private keys, write them to file
#   Will not be necessary in practice
def gen_keys():
    for count in range(len(egress_inventory)):
        private = RSA.generate(1024)
        public = private.publickey()
        FILE_BASE = str(egress_inventory[count]['name'])
        RSA_BASE = str(FILE_BASE + '.rsa')
        PUB_BASE = str(FILE_BASE + '.known_hosts')
        SIG_FILE = os.path.join(KEYFILE, RSA_BASE)
        PUBKEY_FILE = os.path.join(KEYFILE, PUB_BASE)
        with open(SIG_FILE, 'w') as f:
            f.write(private.exportKey())
        with open(PUBKEY_FILE, 'w') as f:
            f.write(public.exportKey())

#Replace ports with port plus count to validate which server is being used
#   Will not be necessary in practice
def replace_ports():
    for count in range(len(egress_inventory)):
        egress_inventory[count]['port'] = (egress_inventory[count]['port'] + (count * count))
    with open('/share/inventory/egress_inventory.json', 'w') as f:
        f.write(simplejson.dumps(egress_inventory, indent=4))
#Menu to change the forward information
def change_menu():
    print "This is the change menu."
    print "Which would you like to change"
    print "1. Change the IP address"
    print "2. Change the port"
    while True:
        try:
            menu_choice = int(raw_input("Please choose one: "))
            if menu_choice == (1 | 2):
                return menu_choice
        except:
            print "Please make a choice"

#TODO Function to Iterate through VPS


#Iterate through forward VPS
def iterate_sshfwd():
    with open(FWD_INV) as f:
        sshfwd_inv = json.load(f)
    for i in range(len(sshfwd_inv)):
        print "%d. %s %s : %d" % ((i+1), sshfwd_inv[i]['name'], sshfwd_inv[i]['ip'], sshfwd[i]['port'])
    return sshfwd_inv

#TODO Change IP Address
#TODO Change port

#Give the user the ability to replace the IPs and Ports
#Needs more input validation
def change_sshfwd():
    while True:
        iterate_sshfwd()
        main_choice = change_menu()
        if main_choice == 1:
            while True:
                iterate_sshfwd()
                try:
                    ip_choice = str(raw_input("Please enter the new IP Address: "))

