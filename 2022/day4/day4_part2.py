# Read in assignment input and store in string
with open('day4_input') as f:
    contents = f.read()

# Split input lines into array
inputArray = contents.splitlines()

# Initialize variables
overlap = 0

# For each pair of inputs, split each input into lists fo easy reference
for pair in inputArray:
    counted = 0
    pairSplit = pair.split(',')
    first = pairSplit[0].split('-')
    second = pairSplit[1].split('-')
    # Check if any of the beginning and ends overlap with eachother
    if int(first[0]) <= int(second[0]) <= int(first[1]):
        overlap += 1
    elif int(first[0]) <= int(second[1]) <= int(first[1]):
        overlap += 1
    elif int(second[0]) <= int(first[0]) <= int(second[1]):
        overlap += 1
    elif int(second[0]) <= int(first[1]) <= int(second[1]):
        overlap += 1

# Return number of overlapping assignments
print(overlap)