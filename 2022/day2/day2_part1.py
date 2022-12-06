# Read in assignment input and store in string
with open('day2_example') as f:
    contents = f.read()

# Split input lines into array
inputArray = contents.splitlines()

totalScore = 0

for i in inputArray:
    roundScore = 0
    if i[2] == 'X':
        roundScore += 1
        if i[0] == 'A':
            roundScore += 3
        elif i[0] == 'B':
            roundScore += 0
        elif i[0] == 'C':
            roundScore += 6
    elif i[2] == 'Y':
        roundScore += 2
        if i[0] == 'A':
            roundScore += 6
        elif i[0] == 'B':
            roundScore += 3
        elif i[0] == 'C':
            roundScore += 0
    elif i[2] == 'Z':
        roundScore += 3
        if i[0] == 'A':
            roundScore += 0
        elif i[0] == 'B':
            roundScore += 6
        elif i[0] == 'C':
            roundScore += 3
    else:
        print('Incorrect input detected')
    print(roundScore)
    totalScore += roundScore

print(totalScore)