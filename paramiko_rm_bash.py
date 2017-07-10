'''
    from https://gist.github.com/batok/2352501
    The intent is for this to set up an ssh connection through paramiko
    We first have to determine if paramiko will work in practice

'''


import paramiko

logfile = '/share/logfiles/sshfwd-01'

k = paramiko.RSAKey.from_private_key_file('/share/inventory/keys/sshfwd-01.rsa')

c = paramiko.SSHClient()

c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print 'CONNECTING'

c.connect( hostname = '192.168.235.133', username = 'sshfwd-01', pkey = k, port = 3030)

print 'CONNECTED!'

commands = [ 'cat .bash_history', 'rm .bash_history' ]

for command in commands:
    print 'Executing {}'.format(command)
    stdin, stdout, stderr = c.exec_command(command)
    with open(logfile, 'a') as f:
        f.write(stdout.read())
    print stdout.read()
    print( "ERRORS")
    print stderr.read()

c.close
