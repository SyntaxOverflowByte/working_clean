#!/usr/bin/python

'''
   The intent of this script is to set up an ssh forward to another server
   This will be to the sshfwd server

'''

import os
import json




INV_ROOT = os.path.join('/share/', 'inventory/')
FWD_INV = os.path.join(INV_ROOT, 'inventory.json')
FWD_KEYS = os.path.join(INV_ROOT, 'keys/')

#Load inventory.json into memory

def fwd_inv():
    with open(FWD_INV) as f:
        sshfwd_inv = json.load(f)
    return sshfwd_inv


