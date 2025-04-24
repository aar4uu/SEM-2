import pandas as pd

# Take input from user
n = int(input("Enter the number of cars: "))

print("Enter asking prices (space-separated):")
asking_input = list(map(float, input().split()))

print("Enter fair prices (space-separated):")
fair_input = list(map(float, input().split()))

# Validate input length
if len(asking_input) != n or len(fair_input) != n:
    print("Error: Number of prices entered does not match the number of cars.")
else:
    # Create pandas Series
    asking_prices = pd.Series(asking_input)
    fair_prices = pd.Series(fair_input)

    # Identify good deals
    good_deals = asking_prices < fair_prices
    good_deal_indices = list(good_deals[good_deals].index)

    # Output
    print("Indices of good deals:", good_deal_indices)
