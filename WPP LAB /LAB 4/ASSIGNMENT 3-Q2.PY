import math

"""TO CHCEK NO IS PERFECTB SQ OR NOT"""
def perfectSq(no):
    x= int(math.sqrt(no))
    return x*x ==no

"""checking the no, if it's in fibonacci no or not"""
def fibonacci(n):
    return perfectSq(5 * n * n + 4) or perfectSq(5 * n * n - 4)


"""Taking input from user"""
T = int(input("Enter how many numbers to be checked: "))

"""logic"""
for _ in range(T):
    N = int(input("Enter a number: "))
    if fibonacci(N):
        print("IsFibo")
    else:
        print("IsNotFibo")

