def myLen(e):
    return len(e)

# Read in assignment input and store in string
with open('day3_example') as f:
    contents = f.read()

# Split input lines into array
inputArray = contents.splitlines()
priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
prioritySum = 0
groups = []

groupCounter = 1

# Create array groups from input
while (groupCounter * 3) <= len(inputArray):
    groupEnd = groupCounter * 3
    groupCounter += 1
    groups.append([inputArray[groupEnd-3],inputArray[groupEnd-2],inputArray[groupEnd-1]])

for group in groups:
    group.sort(key=myLen)
    match = ''

    for i in group[0]:
        positionOne = group[1].find(i)
        if positionOne != -1:
            positionTwo = group[2].find(i)
            if positionTwo != -1:
                match = group[2][positionTwo]

    prioritySum += priority.find(match)+1

print(prioritySum)