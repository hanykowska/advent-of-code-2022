
f = open('2022-12-01.csv','r')

calories = []
summed_calories = []
current_calories = []

for line in f:
    line = line.replace('\n','')
    if line == '':
        calories.append(current_calories)
        summed_calories.append(sum(current_calories))
        current_calories = []
    else:
        current_calories.append(int(line))

f.close()

print(max(summed_calories))

summed_calories.sort()
print(summed_calories[-3:])
print(sum(summed_calories[-3:]))