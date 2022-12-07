def myLen(e):
    return len(e)

# Read in assignment input and store in string
with open('day4_example') as f:
    contents = f.read()

# Split input lines into array
inputArray = contents.splitlines()

fullyContains = 0

for pair in inputArray:
    split = pair.split(',')
    rangeOne = ''.join(map(str,list(range(int(split[0][0]),int((split[0][2]))+1,1))))
    rangeTwo = ''.join(map(str,list(range(int(split[1][0]),int((split[1][2]))+1,1))))
    if len(rangeOne) <= len(rangeTwo):
        if rangeTwo.find(rangeOne) != -1:
            fullyContains += 1
    else:
        if rangeOne.find(rangeTwo) != -1:
            fullyContains += 1

print(fullyContains)