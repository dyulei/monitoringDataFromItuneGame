values = 'a=hello&b=world'
# values = url.split('?')[-1]

e = {}
for key_value in values.split('&'):
	e[key_value.split('=')[0]] = key_value.split('=')[1]
print e


