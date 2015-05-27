"""
same socket, but talk between independent programs too, not just threads;
server here runs in a process and server both process and thread clients;
sockets are machine-global, much like fifos: don't require shared memory
"""

from socket_preview import server, client
import sys, os
from threading import Thread

mod = int(sys.argv[1])
if mod == 1:
	server()
elif mod == 2:
	client('client:process=%s' % os.getpid())
else:
	for i in range(5):
		Thread(target=client, args=('client:thread=%s' % i,)).start()