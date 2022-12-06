# Read in assignment input and store in string
with open('day3_example') as f:
    contents = f.read()

# Split input lines into array
inputArray = contents.splitlines()
priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
prioritySum = 0


for i in inputArray:
    half = int(len(i)/2)
    compartmentOne = i[0:half]
    compartmentTwo = i[half:len(i)]
    sameItem = ''
    for i in compartmentOne:
        position = -1
        position = compartmentTwo.find(i)
        if position != -1:
            sameItem = compartmentTwo[position]
    prioritySum += priority.find(sameItem)+1

print(prioritySum)