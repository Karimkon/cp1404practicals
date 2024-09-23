num_items = int(input("Number of items that were bought: "))

# Error checking for number of items entered in the system.
while num_items < 0:
    print("Invalid number of items!")
    num_items = int(input("Number of items: "))

total_price = 0

# Loop to get the price of each item that the administrater entered in the first place.
for i in range(num_items):
    price = float(input(f"Price of item {i + 1}: "))

# Check for discount
if total_price > 100:
    total_price *= 0.90
print(f"Total price for {num_items} items is ${total_price:.2f}")