bigNum = 600851475143
factors = []
nonPrimeFactors = []
counter = 3

while(counter <= bigNum/3):
	if(bigNum % counter == 0):
		j = bigNum / counter
		if( counter > j ):
			break
		factors.append(j)
		factors.append(counter)
	counter += 2
factors.sort()


for fac in factors:
	counter = 3
	while(counter < fac):
		if(fac % counter == 0):
			nonPrimeFactors.append(fac)
			break
		counter += 2
	
primeFactors = [x for x in factors if x not in nonPrimeFactors]
print(primeFactors)