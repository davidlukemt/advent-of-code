def myLen(e):
    return len(e)

# Read in assignment input and store in string
with open('day3_input') as f:
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

# Itterate through groups, sort them by length
for group in groups:
    group.sort(key=myLen)
    match = ''

# Itterate through the shortest group member to find a common character in the group
    for i in group[0]:
        positionOne = group[1].find(i)
        if positionOne != -1:
            positionTwo = group[2].find(i)
            if positionTwo != -1:
                match = group[2][positionTwo]

# After identifing the common character, determine it's priority value based on the priority string above 
# the characters priority is its position in the priority string starting with a in position 1
# Add all of the priorites together
    prioritySum += priority.find(match)+1

# Return the sum of all groups priorities
print(prioritySum)