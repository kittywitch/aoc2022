with open("input.txt") as f:
    input = f.read().splitlines()

def inclusive_range(start, end):
    return range(start, end+1)

sets = 0
intersects = 0
for line in input:
    elves = [elf.split("-") for elf in line.split(",")]
    elves = [list(map(int, lst)) for lst in elves]
    elf_ranges = [set(inclusive_range(*tuple(elf))) for elf in elves]
    elf_subset = elf_ranges[0].issubset(elf_ranges[1])
    elf_subset2 = elf_ranges[1].issubset(elf_ranges[0])
    elf_intersection = elf_ranges[0].intersection(elf_ranges[1])
    if elf_intersection != set():
        intersects += 1
    enclosed = elf_subset or elf_subset2
    sets += int(enclosed)
    print(enclosed)
print(sets)
print(intersects)
