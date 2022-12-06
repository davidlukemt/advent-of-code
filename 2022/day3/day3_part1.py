# Read in assignment input and store in string
with open('day3_input') as f:
    contents = f.read()

# Split input lines into array
inputArray = contents.splitlines()
priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
prioritySum = 0

# Itterate through the list, split the input string in half and find the character that appears in each half
# After identifing the common character, determine it's priority value based on the priority string above 
# the characters priority is its position in the priority string starting with a in position 1
# Add all of the priorites together
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

# Print the sum of all priorities
print(prioritySum)