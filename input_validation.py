import pdb

pdb.set_trace()

def test():
	print('test')
	a = 20

age = 18

while age > 17:
	test()
	age = input("Age : ")
	try:
		age = int(age)
		if age > 17:
			print('You are a subject to law.')
	except:
		print('Must number.')
		age = 18

print('You are a loly.')
