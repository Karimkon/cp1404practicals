def lists_to_dict(keys, values):
    """Convert two parallel lists into a dictionary."""
    return dict(zip(keys, values))


names = ["Jack", "Jill", "Harry"]
dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

result = lists_to_dict(names, dates_of_birth)
print(result)
