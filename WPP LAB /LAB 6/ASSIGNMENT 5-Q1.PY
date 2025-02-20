def max_xor(L, R):
    max_xor = 0
    for a in range(L,R+1):
        for b in range(a, R+1):
            max_xor= max(max_xor, a ^ b)
    return max_xor

print(" Enter the lower bound: ")
L = int(input())

print(" Enter the upper bound: ")
R = int(input())

print ("Result:" , max_xor(L, R ))

