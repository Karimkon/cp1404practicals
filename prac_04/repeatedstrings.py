def collect_strings():
    strings = {}
    while True:
        user_input = input("Enter a string (or press enter to finish): ")
        if user_input == "":
            break
        strings[user_input] = strings.get(user_input, 0) + 1

    repeated = [s for s, count in strings.items() if count > 1]
    if repeated:
        print("Strings repeated:", ", ".join(repeated))
    else:
        print("No repeated strings entered.")

collect_strings()
