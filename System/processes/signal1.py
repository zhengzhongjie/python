"""
catch singnals in Python; pass singnal number N as a command-line arg,
use a "kill -N pid" shell command to send this process a signal; most
signal handlers restored by Python atfer caught (see network scripting
chapter for SIGCHLD details); on Windows, signal module is available,
but it defines only a few signal types there, and os.kill iis missing;
"""

import sys, signal, time
def now(): return time.ctime(time.time())

def onSingnal(signum, stackFrame):
	print('Got signal', signum, 'at', now())

signum = int(sys.argv[1])
signal.signal(signum, onSingnal)
while True: signal.pause()