#!/usr/bin/python
'''
    Initial attempt to iterate through the JSON file
'''

import JSON
import os
from Crypto.PublicKey import RSA


INV_ROOT = os.path.join('/share/', 'inventory/')
EGRESS_INV = os.path.join(INV_ROOT, 'egress_inventory.json')
KEYFILE = os.path.join(INV_ROOT, 'egress_keys/')

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
    user_choice = (raw_input("Please choose one: ") - 1)
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








