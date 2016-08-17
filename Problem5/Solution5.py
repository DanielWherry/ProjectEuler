dividend = 20
notFound = True

while(notFound):
	for i in range(2,21):
		if(dividend % i != 0):
			break
		elif(20 == i and dividend % i == 0):
			print(str(dividend))
			notFound = False # We love double negatives
	dividend += 20