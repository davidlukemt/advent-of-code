def myLen(e):
    return len(e)

# Read in assignment input and store in string
with open('day4_example') as f:
    contents = f.read()

# Split input lines into array
inputArray = contents.splitlines()

# Initialize variables
fullyContains = 0

# For each pair of inputs, format them to strings of sequential numbers
for pair in inputArray:
    pairSplit = pair.split(',')
    first = pairSplit[0].split('-')
    second = pairSplit[1].split('-')
    if first[0] <= second[0]:
        if first[1] >= second[1]:
            fullyContains += 1
    elif second[0] <= first[0]:
        if second[1] >= first[1]:
            fullyContains += 1

# Return number of fully contained assignments
print(fullyContains)