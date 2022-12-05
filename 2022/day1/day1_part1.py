# Read in assignment input and store in string
with open('day1_input') as f:
    contents = f.read()

# Split input lines into array
inputArray = contents.splitlines()

# Initialize variables
count = 0
elfNum = 0
elfCal = 0
elfTotes = []
moochTarget = 0
moochTargetCal = 0

# Add up all elf calorie totals and store in array,
# track the elf number and totes with the largest 
# calorie count as mooch target
for i in inputArray:
    if(count == len(inputArray)-1):
        elfCal += int(i)
        elfTotes.append(elfCal)
        if elfCal > moochTargetCal:
            moochTarget = elfNum
            moochTargetCal = elfCal
    elif i != '':
        elfCal += int(i)
        count += 1
    elif (i == ''):
        elfTotes.append(elfCal)
        if elfCal > moochTargetCal:
            moochTarget = elfNum
            moochTargetCal = elfCal
        elfNum += 1
        elfCal = 0
        count += 1
    

# Print the mooch target and how many calories they're carrying
print("The Elf to mooch from is:", moochTarget+1)
print("They're carrying",moochTargetCal,"calories!")