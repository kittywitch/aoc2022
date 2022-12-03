import string

with open("input.txt") as f:
    input = f.read().splitlines()

priorities = string.ascii_lowercase + string.ascii_uppercase

total_priority = 0
for bag in input:
    half = len(bag) // 2
    front = bag[half:]
    back = bag[:half]
    common = set(front).intersection(set(back))
    print(common)
    for item in common:
        item_priority = priorities.index(item) + 1
        print(f"{total_priority} += {item_priority} = {total_priority + item_priority}")
        total_priority += item_priority


total_priority = 0
for i in range(0, len(input), 3):
    common = set(input[i]).intersection(set(input[i+1])).intersection(set(input[i+2]))
    print(common)
    for item in common:
        item_priority = priorities.index(item) + 1
        print(f"{total_priority} += {item_priority} = {total_priority + item_priority}")
        total_priority += item_priority
