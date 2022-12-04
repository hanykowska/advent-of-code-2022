f = open('2022-12-04.txt', 'r')
f2 = open('2022-12-04-example.txt', 'r')

# print(f.readline())
# print(f2.readline())

lines = f.readlines()
fully_contained_count = 0
any_overlap_count = 0

for i, line in enumerate(lines):
    line = line.rstrip('\n')
    elf1, elf2 = line.split(',')
    elf1_range = elf1.split('-')
    elf2_range = elf2.split('-')
    for r, e1_r in enumerate(elf1_range):
        elf1_range[r] = int(elf1_range[r])
        elf2_range[r] = int(elf2_range[r])

    # this code is needed for part 2, decided it's easier
    # to go through each element one by one, compared to previous approach.
    elf1 = list(range(elf1_range[0], elf1_range[1]+1))
    elf2 = list(range(elf2_range[0], elf2_range[1]+1))
    round_overlap = 0
    for section in elf1:
        if section in elf2:
            round_overlap = 1
            break
    any_overlap_count += round_overlap
    # end of part 2 code
    
    # part 1 approach:
    # find out which elf has the smaller assignment - they can be contained by the other
    # then check if the start and end point of their range is within the other
    # stop executing this loop and continue to the next.
    elf1_range_len = elf1_range[1] - elf1_range[0] + 1
    elf2_range_len = elf2_range[1] - elf2_range[0] + 1
    if elf1_range_len <= elf2_range_len:
        if (elf1_range[0] >= elf2_range[0] and
            elf1_range[1] <= elf2_range[1]):
            fully_contained_count += 1
            continue
    elif elf2_range_len <= elf1_range_len:
        if (
            elf2_range[0] >= elf1_range[0] and
            elf2_range[1] <= elf1_range[1]
            ):
            fully_contained_count += 1
            continue

print(fully_contained_count)
print(any_overlap_count)