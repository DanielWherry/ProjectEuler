# Skipped check of first two primes, 2 and 3
counter = 5
otherCounter = 3
primeCounter = 0

while(True):
	while(otherCounter < counter):
		if(counter % otherCounter == 0):
			break
		elif((otherCounter == counter - 2) and (counter  % otherCounter != 0)):
			primeCounter += 1
			break
		otherCounter += 2 #No use having even divisors!
		
	if (primeCounter == 9999): # Only going to 9999 because I skipped first two primes
		break
		
	otherCounter = 3
	counter += 2 # No use checking even dividends!
	
print("Prime counter: " + str(primeCounter))
print("Prime number is: " + str(counter))
