# String Formatt
model = "1922 Gibson L-5 CES"
price = 16036
print(f"{model} for about ${price:,.2f}!")

# Using a for loop with f-string formatting
for i in range(11):
    print(f"2 ^ {i} is {2 ** i:>6}")
