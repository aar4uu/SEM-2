""" write a program that ask the user to enter a word and then capitalizes every other letter of
that word. So, if the word is rhinoceros, the program should print rHiNoCeRoS."""

#Taking input from the user.
word = input("Enter the word: ")

result = ""

#Logic 
for i in range(len(word)):
    if i%2 == 0:
        result = result + word[i].lower()
    else:
        result = result + word[i].upper()

print(result)  
    
