LOWER = 33
UPPER = 127

columns = int(input("How many columns do you want to print? "))

# ASCII table display
print(f"{'ASCII':<5}", end="")
for col in range(columns):
    print(f"{'Character':<10}", end="")
print()  # New line after header

for i in range(LOWER, UPPER + 1):
    print(f"{i:<5} {chr(i):<10}", end="")
    if (i - LOWER + 1) % columns == 0:
        print("/n")
