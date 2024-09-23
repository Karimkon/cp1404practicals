name = input("What is your name? ")
name_file = open('name.txt', 'w')
name_file.write(name)

name_file = open('name.txt', 'r')
name_from_file = name_file.read()
name_file.close()
print("Hi " + name_from_file + "!")

with open('numbers.txt', 'r') as numbers_file:
    first_number = int(numbers_file.readline())
    second_number = int(numbers_file.readline())
    sum_of_first_two = first_number + second_number
    print("The sum of first two numbers is: " + str(sum_of_first_two))

with open('numbers.txt', 'r') as numbers_file:
    total = 0
    for line in numbers_file:
        total += int(line)
    print(total)