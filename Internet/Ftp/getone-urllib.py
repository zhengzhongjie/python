#!/usr/local/bin/python

import os, getpass
from urllib.request import urlopen
filename = 'monkeys.jpg'
password = getpass.getpass('Pswd?')

remoteaddr = 'ftp://lutz:%sftp.rmi.net/%s;type=i' % (password, filename)
print('Downloading', remoteaddr)

remotefile = urlopen(remoteaddr)
localfile  = open(filename, 'wb')
localfile.write(remotefile.read)
localfile.close()
remotefile.close()