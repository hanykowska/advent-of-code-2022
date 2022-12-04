f = open('2022-12-03.csv', 'r')

def get_priority(letter):
    if ord(letter) >= 97:
        subtr = -96
    else:
        subtr = -65 + 27
    return ord(letter) + subtr

lines = f.readlines()
priorities = []
badge_priorities = []   # pat two of the challenge

for i,line in enumerate(lines):
    line = line.rstrip('\n')
    
    middle = int(len(line)/2)
    rucksack_1 = line[0: middle]
    rucksack_2 = line[middle:]

    for item in rucksack_1:
        if item in rucksack_2:
            priorities.append(get_priority(item))
            break

for i, line in enumerate(lines):
    if i > len(lines)-3:
        break
    if i % 3:
        continue
    
    for item in line:
        if item in lines[i+1] and item in lines[i+2]:
            badge_priorities.append(get_priority(item))
            break


print(sum(priorities))
print(sum(badge_priorities))