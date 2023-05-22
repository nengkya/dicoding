age = 18

while age > 17:
	age = input("Age : ")
	try:
		age = int(age)
		if age > 17:
			print('You are a subject to law.')
	except:
		print('Must number.')
		age = 18

print('You are a loly.')
