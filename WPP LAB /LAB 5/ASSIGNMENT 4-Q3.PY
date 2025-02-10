def pangram(s):
    alphabet = set("abcdefghijklmnopkrstuvwxyz")
    s=s.lower() #convert to lowercase in any case.
    return alphabet.issubset(set(s)) #check if all letters are in the string.

#input
s= input("Enter the sentence: ")

#output
if pangram(s):
    print("IS PANGRAM")
else:
    print("NOT PANGRAM")
