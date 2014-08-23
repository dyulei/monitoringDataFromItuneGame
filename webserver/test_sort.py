

def cmp1(x, y):
	if x[1] > y[1]:
		return 1
	elif x[1] < y[1]:
		return -1
	else: return 0


def cmp2(x, y):
	if x['id'] > y['id']:
		return 1
	elif x['id'] < y['id']:
		return -1
	else: return 0


A = [[66,4], [100,3], [88,2], [99,1]]
B = [
	{
        "id": 1,
        "text": "",
        "icon" : "httml...",
        "num" : 20
    },
    {
        "id": 3,
        "text": "",
        "icon" : "httml...",
        "num" : 20
    },
    {
        "id": 2,
        "text": "",
        "icon" : "httml...",
        "num" : 20
    },
    {
        "id": 4,
        "text": "",
        "icon" : "httml...",
        "num" : 20
    }
]
# B.sort(cmp=cmp2)
B.sort(cmp=cmp2)
print B