from collections import Counter

# Read in assignment input and store in string
with open('day6_example') as f:
    contents = f.read()

# Split input lines into array
inputArray = contents.splitlines()

# Itterate through input file lines
for item in inputArray:
    i = 0
    markerFound = False

    # Itterate through line looking at 4 character segments
    while i+4 < len(item) and not markerFound:
        fourChar = item[i:i+14]
        keepGoing = True
        charIndex = 0
        
        # Check the four character segment for duplicate characters, if none found return that segment as the marker
        while keepGoing:
            char = fourChar[charIndex]
            if fourChar.count(char) != 1:
                keepGoing = False
            elif charIndex == 13:
                keepGoing = False
                markerFound = True
                print(fourChar)
            else:
                charIndex += 1
        if markerFound != True:
            i += 1

    print("Marker in", item, "located at",i+14)