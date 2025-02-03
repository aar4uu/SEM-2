def growth(n):
    height = 1 #initial height.

    for cycle in range (1, n+1):

        #monsoon  cycle - double height.
        if cycle % 2==1: 
            height = height * 2
        #summer cycle - increases by 1 meter.
        else:
            height = height +1 

    return height

#taking input 
N = int(input("Enter the no of tress to be checked: "))

for _ in range(N):
    no= int(input("Enter the no of cycles: "))
    print(growth(no))
