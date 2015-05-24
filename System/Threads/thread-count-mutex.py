"""
syschronize access to stdout: because it is shared global,
thread output may be intermixed if not syschronized
"""
import _thread as thread, time

def counter(myId, count):
	for i in range(count):
		time.sleep(1)
		mutex.acquire()
		print('[%s] => %s' % (myId, i))
		mutex.release()

mutex = thread.allocate_lock()
for i in range(5):
	thread.start_new_thread(counter, (i, 5))

time.sleep(6)
print('Main thread exiting.')