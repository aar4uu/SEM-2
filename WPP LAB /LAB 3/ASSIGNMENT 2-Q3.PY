"""Find Digits
You are given a number N, you need to print the number of positions where digits exactly 
divides N."""

#Taking input from the user for how many numbers to be test performed.
numbers = int(input("Enter the numbers test to be performed: "))

#logic
for _ in range(numbers):
    n = int(input("Enter the number: "))
    count = 0
    number_str = str(n) #converting it to string

    for digit in number_str:
        if digit == '0': #skip division by 0
            continue
        if n % int(digit)==0: #check if digit divides the n
            count = count + 1

print(count)

