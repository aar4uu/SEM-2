""" You are a student in a class of 10. Your class teacher assigns you a task of entering the 
names of all the students in the class. You finally want to display the names given the 
condition that the maximum allowed characters in a name is 15. As a fun task, reverse the 
names and display them. [Hint: Slicing works when you are selecting maximum characters] """
 

# Initialize an empty list to store the names
students = []

# Number of students in the class
num_students = 10

print("Enter the names of 10 students (maximum 15 characters per name):")

# Loop to input student names
for i in range(num_students):
    while True:
        name = input(f"Enter the name of student {i + 1}: ")
        if len(name) <= 15:
            students.append(name)
            break
        else:
            print("Name exceeds 15 characters. Please try again.")

# Reverse the names and display them
print("\nReversed Names:")
for name in students:
    print(name[::-1])