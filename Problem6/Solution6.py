sumOfSquares = 0
squareOfSum = 0
sumOfFirstHundred = 0

for i in range(1, 101):
	sumOfSquares += i**2
for i in range(1,101):
	sumOfFirstHundred += i
squareOfSum = sumOfFirstHundred**2

diff = squareOfSum - sumOfSquares

print(str(diff))