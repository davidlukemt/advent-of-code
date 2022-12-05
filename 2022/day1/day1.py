# Read in assignment input and store in string
with open('day1_example') as f:
    contents = f.read()

# Split input lines into array
inputArray = contents.splitlines()

# Initialize variables
elfNum = 0
elfCal = 0
elfTotes = []
moochTarget = 0
moochTargetCal = 0

# Add up all elf calorie totals and store in array,
# track the elf number and totes with the largest 
# calorie count as mooch target
for i in inputArray:
    if i != '':
        elfCal += int(i)
    else:
        elfTotes.append(elfCal)
        if elfCal > moochTargetCal:
            moochTarget = elfNum
            moochTargetCal = elfCal
        elfNum += 1
        elfCal = 0

# Print the mooch target and how many calories they're carrying
print("The Elf to mooch from is:", moochTarget+1)
print("They're carrying",moochTargetCal,"calories!")