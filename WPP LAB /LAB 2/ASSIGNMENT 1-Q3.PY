"""Write a program that asks the user to enter a length in feet. The program should then give 
the user the option to convert from feet into inches, yards, miles, millimeters, centimeters, 
meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they 
enter a 2, then the program converts to yards, etc. While this can be done with if statements, 
it is much shorter with lists and it is also easier to add new conversions if you use lists. """


# Conversion factors from feet to various units
conversion_factors = [
    ("inches", 12),
    ("yards", 1/3),
    ("miles", 1/5280),
    ("millimeters", 304.8),
    ("centimeters", 30.48),
    ("meters", 0.3048),
    ("kilometers", 0.0003048),
]

# Display options to the user
print("Choose a conversion option:")
for i, (unit, _) in enumerate(conversion_factors, start=1):
    print(f"{i}. Convert to {unit}")

# Input length in feet
while True:
    try:
        feet = float(input("\nEnter the length in feet: "))
        if feet < 0:
            print("Length cannot be negative. Try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Input conversion option
while True:
    try:
        choice = int(input("Enter your choice (1-7): "))
        if 1 <= choice <= len(conversion_factors):
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Perform the conversion
selected_unit, factor = conversion_factors[choice - 1]
converted_value = feet * factor

# Output the result
print(f"\n{feet} feet is equal to {converted_value:.4f} {selected_unit}.")