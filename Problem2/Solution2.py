theSum = 0
startingValue = 1
nextValue = 2

while True:
    if startingValue % 2 == 0:
       theSum += startingValue
    elif nextValue % 2 == 0:
       theSum += nextValue
  
    if nextValue >= 4000000:
       break

    startingValue += nextValue
    nextValue += startingValue
    
print theSum
