# ANSWER:give n a random number between 1 to 100.
# if it is lager than number stoerd in the stored_random_number(the origin number is 0)
# the number in n would be stored in the stored_random_number
# this process continues 10 times(0 to 9)

progress=0
stored_random_number=0
while progress<10:
	progress+=1
	n = randint(1,100)
	if n > stored_random_number:
		stored_random_number = n

print(stored_random_number)
