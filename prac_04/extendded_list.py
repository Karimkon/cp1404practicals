def collect_numbers():
    numbers = []
    count = 1
    while True:
        number = float(input(f"Number {count}: "))
        if number < 0:
            break
        numbers.append(number)
        count += 1

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.2f}")

collect_numbers()
