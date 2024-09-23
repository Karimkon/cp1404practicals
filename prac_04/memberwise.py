def add_memberwise(list1, list2):
    length = min(len(list1), len(list2))
    return [list1[i] + list2[i] for i in range(length)] + list1[length:] + list2[length:]

print(add_memberwise([1, 2, 3], [4, 7, 11]))
print(add_memberwise([1, 2, 3], [1, 7, 3, 9]))
