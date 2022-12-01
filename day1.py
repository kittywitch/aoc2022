import collections

with open("input.txt") as f:
    elf_log = f.read().splitlines()

elves = collections.defaultdict(list)

elf_count = 0
for log_index in range(0, len(elf_log)):
    calories = elf_log[log_index]
    if calories != "":
        elves[elf_count].append(int(calories))
    else:
        elf_count += 1

elves_total = {elf : sum(calories) for (elf, calories) in elves.items()}

print(elves)
print(elves_total)

# Task 1
print("Task 1")
hauler = max(elves_total, key=elves_total.get)
print(f"Elf {hauler} has the most calories with {elves_total[hauler]}")

# Task 2
print("Task 2")
most = []
for i in range(0, 3):
    hauler = max(elves_total, key=elves_total.get)
    most.append(elves_total[hauler])
    del elves_total[hauler]
print(f"The five elves carrying the most calories are carrying: {sum(most)} amongst themselves.")
