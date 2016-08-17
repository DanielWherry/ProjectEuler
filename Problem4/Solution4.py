numInText = ""
numBackwards = ""
palindromes = []

list = range(100,1000)
reversed = list[::-1]

for i in range(100,1000):
	for j in range(100,1000):
		num = i * j
		numInText = str(num)
		numBackwards = numInText[::-1]
		if(numInText == numBackwards):
			palindromes.append(num)
palindromes.sort()
length = len(palindromes)
print(palindromes[length - 1])