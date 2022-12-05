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
moochTarget = [0,0,0]
moochTargetCal = [0,0,0]

# Add up all elf calorie totals and store in array,
# track the elf number and totes with the largest 
# calorie count as mooch target
for i in inputArray:
    if(count == len(inputArray)-1):
        elfCal += int(i)
        elfTotes.append(elfCal)
        # Check if this total is greater than the top three and update accordingly
        if elfCal > moochTargetCal[0]:
            moochTarget[2] = moochTarget[1]
            moochTarget[1] = moochTarget[0]
            moochTarget[0] = elfNum+1

            moochTargetCal[2] = moochTargetCal[1]
            moochTargetCal[1] = moochTargetCal[0]
            moochTargetCal[0] = elfCal
        
        elif elfCal > moochTargetCal[1]:
            moochTarget[2] = moochTarget[1]
            moochTarget[1] = elfNum+1

            moochTargetCal[2] = moochTargetCal[1]
            moochTargetCal[1] = elfCal
        
        elif elfCal > moochTargetCal[2]:
            moochTarget[2] = elfNum+1

            moochTargetCal[2] = elfCal
    
    elif i != '':
        elfCal += int(i)
        count += 1
    
    elif (i == ''):
        elfTotes.append(elfCal)
        # Check if this total is greater than the top three and update accordingly
        if elfCal > moochTargetCal[0]:
            moochTarget[2] = moochTarget[1]
            moochTarget[1] = moochTarget[0]
            moochTarget[0] = elfNum+1

            moochTargetCal[2] = moochTargetCal[1]
            moochTargetCal[1] = moochTargetCal[0]
            moochTargetCal[0] = elfCal
        
        elif elfCal > moochTargetCal[1]:
            moochTarget[2] = moochTarget[1]
            moochTarget[1] = elfNum+1

            moochTargetCal[2] = moochTargetCal[1]
            moochTargetCal[1] = elfCal
        
        elif elfCal > moochTargetCal[2]:
            moochTarget[2] = elfNum+1

            moochTargetCal[2] = elfCal
        
        count += 1
        elfNum += 1
        elfCal = 0

print("Top Three Calorie Carriers:",moochTarget)
print("Top Three Calorie Carrier Calories:",moochTargetCal)
print("Sum of Top Three Calorie Carriers:",sum(moochTargetCal))