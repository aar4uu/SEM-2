
def singleDigitSum(no):
    while no >=10:
        no =sum(int(digit)for digit in str(no))
    return no

#taking input from user.
no = int(input("Enter the number: "))
print("singleDigitSum: ",singleDigitSum(no) )