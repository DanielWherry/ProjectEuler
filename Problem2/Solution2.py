theSum = 0
startingValue = 1
nextValue = 2

while True:
    if nextValue >= 4000000:
       break
    
    if startingValue % 2 == 0:
       theSum += startingValue
    elif nextValue % 2 == 0:
       theSum += nextValue
  
    startingValue += nextValue
    nextValue += startingValue
    
print theSum
