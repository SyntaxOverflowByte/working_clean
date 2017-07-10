'''
    from https://gist.github.com/batok/2352501
    The intent is for this to set up an ssh connection through paramiko
    We first have to determine if paramiko will work in practice
    Need to finish this
    https://github.com/paramiko/paramiko/blob/master/demos/forward.py
'''

import os, json, paramiko, time
from Crypto.Random import random

INV_ROOT = os.path.join('/share/', 'inventory/')

REDIR_PATH = os.path.join(INV_ROOT, 'inventory.json')

EGRESS_PATH = os.path.join(INV_ROOT, 'egress_inventory.json')

REDIR_KEYS = os.path.join(INV_ROOT, 'keys/')

EGRESS_KEYS = os.path.join(INV_ROOT, 'egress_keys/')

def load_fwd():
    with open(REDIR_PATH) as f:
        redir = json.load(f)
    return redir

def choose_fwd():
    all_fwd = load_fwd()
    choose = random.randint(0, (len(all_fwd)-1))
    choice = all_fwd[choose]
    return choice

def load_vps():
    with open(EGRESS_PATH) as f:
        egress = json.load(f)
    return egress

def choose_vps():
    egress = load_vps()
    for i in range(len(egress)):
        print "%d. %s %s : %d" % ( (i+1), egress[i]['name'], egress[i]['ip'], egress[i]['port'])
    choose = int(raw_input('Enter a number ')+1)
    choice = egress[choose]
    return choice

fwd_redir = choose_fwd()
chosen_vps = choose_vps()

def fwd_tunnel():
    
    fwd_port = fwd_redir['port']
    fwd_name = fwd_redir['name']
    fwd_ip = fwd_redir['ip']
    rsa_name = str(fwd_name + '.rsa')
    sig_name = str(fwd_name + '.known_hosts')
    rsa_file = os.path.join(REDIR_KEYS, rsa_file)
    sig_file = os.path.join(REDIR_KEYS, sig_name)
    log_dir = os.path.join(INV_ROOT, 'logfile/')
    log_file = os.path.join(log_dir, fwd_name)

    vps_port = chosen_vps['port']
    vps_name = chosen_vps['name']
    vps_ip = chosen_vps['ip']
    
    k = paramiko.RSAKey.from_private_key_file(rsa_file)

    c = paramiko.SSHClient()

    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    print 'CONNECTING'

    c.connect( hostname = fwd_ip, username = fwd_name, pkey = k, port = fwd_port)
    time.sleep(5)
    print 'CONNECTED!'
    
    print 'Default commands will read and remove the bash history, and pull uptime.' 
    print 'Enter additional commands to run.'
    commands = ['cat .bash_history', 'rm .bash_history', 'uptime']
'''
    while != 'q':
        command = str(raw_input("Enter Command to run -> "))
        if len(command) > 1:
            commands.append(command)
            break
        else:
            pass

    for command in commands:
        print 'Executing {}'.format(command)
        stdin, stdout, stderr = c.exec_command(command)
        with open(log_file, 'w') as f:
            f.write(stdout.read())
        print stdout.read()
        print( "ERRORS")
        print stderr.read()

    c.close

'''
    
