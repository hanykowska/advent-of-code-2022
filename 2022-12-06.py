f = open('2022-12-06.txt', 'r')

datastream = f.readlines()[0].rstrip('\n')
# datastream = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
# print(datastream)

four_list = []

for i in range(4, len(datastream)+1):
    four_list = datastream[i-4:i]
    four_set = list(set(four_list))
    if len(four_set) == 4:
        print('start of packet marker:',i)
        break

for i in range(14, len(datastream)+1):
    four_list = datastream[i-14:i]
    four_set = list(set(four_list))
    if len(four_set) == 14:
        print('start of message marker:',i)
        break