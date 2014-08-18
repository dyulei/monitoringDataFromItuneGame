

def cmp1(x, y):
	if x[1] > y[1]:
		return 1
	elif x[1] < y[1]:
		return -1
	else: return 0


A = [[66,4], [100,3], [88,2], [99,1]]
A.sort(cmp=cmp1)
print A