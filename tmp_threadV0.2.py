import threading
import time


num = 0
class myThread(threading.Thread):
	def __init__(self, name, name2):
		threading.Thread.__init__(self)
		self.t_name = name
		self.t_name2 = name2

	def run(self):
		global num
		num = 0
		while True:
			num += 1
			print 'Thread %s Thread %s , Number : %d' % (self.t_name, self.t_name2, num)
			if num > 100:
				print 'dd'
				break


def test():
	thread1 = myThread('A', 'C')
	thread2 = myThread('B', 'D')
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()

test()