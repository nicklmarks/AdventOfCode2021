#!/bin/python3


## Read in file
## parse each line
## determine how many times the depth increases

#### TODO: Read filename from std input as an argument to the program.

print("reading input from file")

file = open('input', 'r')
lines = file.readlines()

# Set base conditions and variables. 
# Set depth to 0.
# Set horizontal to 0.

depth = 0
horizontal = 0


# Loop through each line which represents a movement forward, up or down depth.
# split the line at the space, there will be a word and a number
# forward will increase the horizonal by the number
# up will increase the depth and down will subtract the depth

for line in lines : 
    line = line.strip().split()
    print(line[0] + ' ' +  line[1])
    if line[0] == "forward" :
        print("Moving Forward " + line[1])
        horizontal += int(line[1])
        print("Current Horizontal location is : " + str(horizontal))

    if line[0] == "up" :
        print("Moving Up " + line[1])
        depth -= int(line[1])
        print("Current Depth location is : " + str(depth))

    if line[0] == "down" :
        print("Moving Down " + line[1])
        depth += int(line[1])
        print("Current Depth location is : " + str(depth))

answer = horizontal * depth
print("The answer is : " + str(answer))


#for line in range(0,len(lines)) :
#    print(line)



