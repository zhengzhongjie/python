"""
thread basics: start 5 copies of a function running in parallel;
uses time.sleep so that the main thread doesn't die too earlly--
this kills all other threads on some platforms; stdout is shared:
thread output may be intermixd in this version arbitrarily.
"""
import _thread as thread, time

def counter(myId, count):
	for i in range(count):
		time.sleep(1)
		print('[%s] => %s' % (myId, i))

for i in range(5):
	thread.start_new_thread(counter,(i, 5))

time.sleep(6)
print('Main thread exiting.')