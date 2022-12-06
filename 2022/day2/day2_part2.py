# Read in assignment input and store in string
with open('day2_input') as f:
    contents = f.read()

# Split input lines into array
inputArray = contents.splitlines()

# Initialize variable
totalScore = 0
cleanInput = 1
moveArray = []

# Calculate score based on players and opponents chosen moves
# if anything other than expected input is detected, 
for i in inputArray:
    roundScore = 0
    if i[2] == 'X':
        roundScore += 0
        if i[0] == 'A':
            roundScore += 3
            moveArray.append('Scissors')
        elif i[0] == 'B':
            roundScore += 1
            moveArray.append('Rock')
        elif i[0] == 'C':
            roundScore += 2
            moveArray.append('Paper')
    elif i[2] == 'Y':
        roundScore += 3
        if i[0] == 'A':
            roundScore += 1
            moveArray.append('Rock')
        elif i[0] == 'B':
            roundScore += 2
            moveArray.append('Paper')
        elif i[0] == 'C':
            roundScore += 3
            moveArray.append('Scissors')
    elif i[2] == 'Z':
        roundScore += 6
        if i[0] == 'A':
            roundScore += 2
            moveArray.append('Paper')
        elif i[0] == 'B':
            roundScore += 3
            moveArray.append('Scissors')
        elif i[0] == 'C':
            roundScore += 1
            moveArray.append('Rock')
    else:
        print('Incorrect input detected')
        cleanInput = 0
        break

    print(roundScore)
    totalScore += roundScore

# Check for clean input then output total score    
if cleanInput:
    print(totalScore)
else:
    print('Incorrect input encountered, check input format')