def palindrome(s): #takes input string s as a parameter.
    #n = len(s) #initializes n to the length  of the string.
    operations = 0 #initializes operations that will strore the no of operations.
    
    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] != s[end]:
            #operations = operations + abs(ord(s[start]) - ord(s[end])) #reduces large character.
            operations = operations+1
        start = start + 1
        end = end - 1
    return operations

print( "No of test cases:")
T = int(input()) #no of test cases

print("Input:")
results = []

for _ in range(T):
    s = input().strip()
    results.append(str(palindrome(s)))

print("Output:")

print("\n".join(results))
