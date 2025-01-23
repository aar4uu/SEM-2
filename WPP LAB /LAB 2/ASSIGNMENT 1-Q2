""" Write a program that generates 100 random integers that are either 0 or 1. Then find the 
longest run of zeros, the largest number of zeros in a row. For instance, the longest run of 
zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4. """


#GENERATING RANDOM INTEGERS (0 OR 1) FOR 100 TIMES.

import random 
l=[]
for i in range(100):
    temp = random.randint (0,1)
    l.append(temp)
    print (l[i])

max_zero = 0
count_zero = 0

for i in range(100):
    if l[i]==0:
        count_zero+=1
        if count_zero>max_zero:
            max_zero=count_zero
        
    else:
        count_zero=0
print("Maximum number of consecutive zeroes is:",max_zero)





