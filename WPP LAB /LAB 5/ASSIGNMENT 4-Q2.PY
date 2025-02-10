import math

def sq_integers(A,B):
    count = 0
    for num in range(A , B+1):
        if math.isqrt(num) ** 2 == num:
            count = count+1

    return count
    
print("GIVE THE NO OF TEST CASES: ")
T = int(input())
print("INPUT: ")
results = []

for _ in range(T):
    A, B = map(int, input().split())
    results.append(str(sq_integers(A,B)))

print("OUTPUT: ")
print("\n".join(results))
    

