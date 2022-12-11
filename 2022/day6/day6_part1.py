from collections import Counter

# Read in assignment input and store in string
with open('day6_example') as f:
    contents = f.read()

# Split input lines into array
inputArray = contents.splitlines()

for item in inputArray:
    print(item)
    
    i = 0
    print(item[i:i+4])
    keepGoing = True
    while i+4 < len(item):
        fourChar = item[i:i+3]
        
        print(fourChar)
        
        for letter in fourChar:
            if fourChar.find(letter) != -1:
                keepGoing = False
            else:
                i += 1

    print(i+4)