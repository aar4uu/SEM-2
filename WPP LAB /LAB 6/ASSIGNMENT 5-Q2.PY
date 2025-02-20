def max_pieces(K):
     num1=K//2
     num2=K-num1
     max=num1*num2
     return max
    
    
# Input the number of test cases
print("Enter the no of TEST CASES: ")
testcases = int(input())

l=[]
# For each test case, calculate and print the result
for i in range(testcases):
    n = int(input())  # Number of cuts
    l.append(n) 
for i in l:
    FINAL_PIECES=max_pieces(i)
    print(FINAL_PIECES)
