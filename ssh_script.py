import os, sys, json, shlex, argparse, datetime
import subprocess as sub
from shutil import copyfile

parser = argparse.ArgumentParser(prog='Prog', usage='%(prog)s [options]', description='Arguments to interact with the ssh_script.py')
parser.add_argument('-o', '--outfile', type=str, action='store', help='Pass in the name of the file you want written to in the /tmp directory' )
parser.add_argument('-c', '--command', type=str, action='store', help='Pass in any additional commands you want run - currently only one.')
parser.add_argument('-s', '--server', required=True, type=int, action='store', help='Pass in the server choice')
args = parser.parse_args()

def DTG(fname, fmt='/tmp/{fname}_%Y%m%d_%H.%M.%S'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

def extra_command():
    if args.command:
        command = args.command
    else:
        command = 'uptime'
    return command


def name_file ():
    if args.outfile:
        file_name = str(args.outfile)
        outfile = DTG(file_name)
    else:
        outfile = DTG('test_file')
    return outfile



INV_ROOT = os.path.join('/share/', 'inventory')
KEYS_PATH = os.path.join(INV_ROOT, 'keys')

def inventory():
    inv_path = os.path.join(INV_ROOT, 'inventory.json')
    inv_json = {}
    with open(inv_path) as f:
        inv_json = json.load(f)
    return inv_json

 

def setup_call(num, inv):
    KNOWN_ROOT = os.path.join('/root/', '.ssh', 'known_hosts')
    try:
        os.remove(KNOWN_ROOT)
    except:
	pass
	
    trueip = inv[num]['ip']
    trueport = inv[num]['port']
    server_name = inv[num]['name']
    KNOWN_FILE = server_name + '.known_hosts'
    KNOWN_PATH = os.path.join(KEYS_PATH, KNOWN_FILE)
    copyfile(KNOWN_PATH, KNOWN_ROOT)
	
    return trueip, trueport, server_name

def build_ssh(port, path, name, ip):
    cmd = 'ssh '
    cmd += '-p %d ' % port
    cmd += '-i %s ' % path
    cmd += '%s@%s ' % (name, ip)
    return cmd
	

def make_call(server, command):
    num = server
# Make out_file
    out_file = name_file()
# Populate inventory
    inv = inventory()
# Setup the variables
    ip, port, name = setup_call(num, inv)
    KEY_FILE = name + '.rsa'
    KEY_PATH = os.path.join(KEYS_PATH, KEY_FILE)
    base_command = build_ssh(port, KEY_PATH, name, ip)
    ssh_command = base_command + ' ' + command
    cmd_v = shlex.split(ssh_command)
    output = sub.check_output(cmd_v, stderr=sub.STDOUT)
    with open(out_file, 'w') as f:
        f.write(output)
#	for line in output:
#            f.write(line)
    return 0


if __name__ == '__main__':
    num = args.server
    command = extra_command()
    make_call(num, command)
	
