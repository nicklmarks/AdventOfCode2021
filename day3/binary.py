#!/bin/python3


## Read in file
## parse each line
## determine how many times the depth increases

#### TODO: Read filename from std input as an argument to the program.

print("reading input from file")

file = open('input', 'r')
lines = file.readlines()


ones = 12 * [0]
#zeroes = 12 * [0]

print(ones)

for line in lines :
    i = 0
    for c in line :
        if c == '1' :
#            print("found 1")
            ones[i] += 1
        i += 1

print(ones)

# ans = 0b0
ans = '' 
zeroes = '' 

for x in ones :
    i = 0
    if x > 500:  
        print("final 1")
        ans += '1'
        zeroes += '0'

    if x < 500: 
        print("final 0")
        ans += '0'
        zeroes += '1'

print(ans)
int_one = (int(ans,2))
print(int_one)

print(zeroes)
int_zero = (int(zeroes,2))
print(int_zero)

final = int(int_one * int_zero)

print("Answer is " + str(final))

# zeroes is ones complement in binary
# ans = ones * zeroes


'''

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


'''
