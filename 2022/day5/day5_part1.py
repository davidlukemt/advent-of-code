# Read in assignment input and store in string
with open('day5_example') as f:
    contents = f.read()

# Split input lines into array
inputArray = contents.splitlines()

# Trim off the container stack
splitFound = False
index = 0
splitPosition = 0

while not splitFound:
    if inputArray[index] == '':
        splitFound = True
        splitPosition = index
    index += 1

stacks = inputArray[:splitPosition]
moves = inputArray[splitPosition+1:]

numberOfStacks = int(stacks[-1][-2])
x = len(stacks)-2
z = 0
easierStacks = []

i = 1

while i <= numberOfStacks:
    easierStacks.append([])
    i += 1

while x >= 0:
    y = 0
    keepGoing = True
    while keepGoing:
        stackPosition = 4*(y+1)-3
        if(stacks[x][stackPosition]) != ' ':
            easierStacks[y].append(stacks[x][stackPosition])
        y += 1
        keepGoing = 4*(y+1)-3 < len(stacks[x])
    x = x - 1
    z += 1

for i in moves:
    line = i.split(' ')
    toMove = int(line[1])
    moveFrom = int(line[3])-1
    moveTo = int(line[5])-1
    x = 0
    while x < toMove:
        moving = easierStacks[moveFrom][(len(easierStacks[moveFrom])-1)]
        easierStacks[moveTo].append(moving)
        easierStacks[moveFrom].pop(-1)
        x += 1

output = ''
for top in easierStacks:
    output += top[-1]

print(output)