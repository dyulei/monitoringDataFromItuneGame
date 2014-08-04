import threading
import time


num = 0
class myThread(threading.Thread):
	def __init__(self, name):
		threading.Thread.__init__(self)
		self.t_name = name

	def run(self):
		global num
		num = 0
		while True:
			num += 1
			print 'Thread %s , Number : %d' % (self.t_name, num)
			if num > 100:
				print 'dd'
				break


def test():
	thread1 = myThread('A')
	thread2 = myThread('B')
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()

test()