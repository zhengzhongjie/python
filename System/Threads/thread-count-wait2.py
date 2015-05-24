"""
uses simple shared global data (not mutexes) to know when threads
are done in parent/main threads; threads share list but not its items,
assumes list won't move in menory once it has been created initially
"""

import _thread as thread
stdoutmutex = thread.allocate_lock()
exitmutexes = [False] * 10

def counter(myId, count):
	for i in range(count):
		stdoutmutex.acquire()
		print('[%s] => %s' % (myId, i))
		stdoutmutex.release()
	exitmutexes[myId] = True

for i in range(10):
	thread.start_new_thread(counter, (i, 100))

while False in exitmutexes: pass
print('Main thread exiting.')