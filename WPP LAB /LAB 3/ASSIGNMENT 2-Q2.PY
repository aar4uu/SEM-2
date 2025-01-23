"""Write a program that repeatedly asks the user to enter product names and prices. Store all 
of these in a dictionary whose keys are the product names and whose values are the prices. 
When the user is done entering products and prices, allow them to repeatedly enter a 
product name and print the corresponding price or a message if the product is not in the 
dictionary."""

products = {}

while True:
    product = input("Enter the product name(or type done to exit): ")
    if product == 'done':
        break
    price = float(input("Enter the price of the product:"))
    products[product]=price

print("\n")
while True:
    product = input(" \n Enter the product name to find the price (or type done to exit):")
    if product == 'done':
        break
    if product in products:
        print(f"The price of {product} is {products[product]}")
    else:
        print(f" {product} is not in the dictionary ")


    
