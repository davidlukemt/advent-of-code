def myLen(e):
    return len(e)

# Read in assignment input and store in string
with open('day4_example') as f:
    contents = f.read()

# Split input lines into array
inputArray = contents.splitlines()

# Initialize variables
overlap = 0

# For each pair of inputs, format them to strings of sequential numbers
for pair in inputArray:
    counted = 0
    pairSplit = pair.split(',')
    first = pairSplit[0].split('-')
    second = pairSplit[1].split('-')
    # Check if second of the pair is contained within the first
    if int(first[0]) <= int(second[0]) <= int(first[1]):
        overlap += 1
    elif int(first[0]) <= int(second[1]) <= int(first[1]):
        overlap += 1
    elif int(second[0]) <= int(first[0]) <= int(second[1]):
        overlap += 1
    elif int(second[0]) <= int(first[1]) <= int(second[1]):
        overlap += 1

# Return number of fully contained assignments
print(overlap)