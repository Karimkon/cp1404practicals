print("Count in 10 from 0 to 100:")
for i in range(0, 100, 10):
    print(i, end=' ')

print("Count down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')

print("Printing stars:")
numbers = int(input("Enter any number you want: "))
for i in range(numbers):
    print('*', end=' ')
