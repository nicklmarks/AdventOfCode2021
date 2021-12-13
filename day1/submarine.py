#!/bin/python3


## Read in file
## parse each line
## determine how many times the depth increases

#### TODO: Read filename from std input as an argument to the program.

print("reading input from file")

file = open('input', 'r')
lines = file.readlines()

# Set base conditions and variables. 
# Set depth to negative because all values should be positive.
# Set counter for the number of depth increases to -1 to account for the first increase being an artifact of this algorithm

num_increases = -1
current_depth = -1


# Loop through each line which represents a depth for the sonar.
# Increase the counter for each depth where depth_1 is > depth_2
# Each loop reset the depth to compare depth(N-1) > depth(N)

for line in lines:
    if int(line) > current_depth :
        num_increases += 1
    current_depth = int(line)

# Print the results

print("count of depth increases = " + str(num_increases))





### Sample Program Below


test_array = [1,2,3,4,5]
print("Array = " + str(test_array))

count = -1
tmp = -1
for i in test_array:
    if i > tmp :
        count += 1

    tmp = i


print("count = " + str(count))

