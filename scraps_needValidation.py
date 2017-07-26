def change_ip_sshfwd():
    ...:     with open(FWD_INV) as f:
    ...:         sshfwd_inventory = json.load(f)
    ...:     print "Which IP Address would you like to change?"
    ...:     for count in range(len(sshfwd_inventory)):
    ...:         print "%d. %s: %s" % ( (count+1), sshfwd_inventory[count]['name'], sshfwd_inventory[count]['ip'])
    ...:     while True:
    ...:         try:
    ...:             choice = (int(raw_input("Choose a number: ")) - 1)
    ...:             break
    ...:         except:
    ...:             print "Please choose one of the numbers on the left"
    ...:     print "You chose: %s: %s" % (sshfwd_inventory[choice]['name'], sshfwd_inventory[count]['ip'])
    ...:     while True:
    ...:         try:
    ...:             new_ip = str(raw_input("Please enter the new IP Address "))
    ...:             sshfwd_inventory[choice]['ip'] = new_ip
    ...:             break
    ...:         except:
    ...:             print "Please enter a valid IP Address"
    ...:     print "Which port would you like to change?"
    ...:     for count in range(len(sshfwd_inventory)):
    ...:         print "%d. %s : IP %s port %d" % ((count + 1), sshfwd_inventory[count]['name'], sshfwd_inventory[count]['ip'], sshfwd_inventory[count]['port'])
    ...:     while True:
    ...:         try:
    ...:             choice = (int(raw_input("Choose a number: ")) - 1)
    ...:             break
    ...:         except:
    ...:             print "Please choose one of the numbers on the left"
    ...:     while True:
    ...:         try:
    ...:             new_port = int(raw_input("Please enter new port: "))
    ...:             sshfwd_inventory[choice]['port'] = new_port
    ...:             break
    ...:         except:
    ...:             print "Please enter a valid integer between 1025 and 65535"
    ...:     with open(FWD_INV, 'w') as f:
    ...:         f.write(simplejson.dumps(sshfwd_inventory, indent=4))
    ...:     return

