f = open('2022-12-05.txt', 'r')
fe = open('2022-12-05-example.txt', 'r')

data = f.readlines()

def get_number_of_stacks(length):
    # remove new line character, one outer 3-character combination, 
    # then divide by 4 (3-character + space)
    return int((length-1-3)/4 + 1)

def get_stack_index(position):

    return int((position-1)/4 + 1)

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        if len(self.__stk) == 0:
            return ' '
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

    def pop_multiple(self, n):
        vals = self.__stk[-n:]
        del self.__stk[-n:]
        return vals

    def push_multiple(self, vals):
        for val in vals:
            self.push(val)

####### initiate stacks
no_stacks = int(get_number_of_stacks(len(data[0])))

stacks = {}
for i in range(no_stacks):
    stacks[i+1] = Stack()

break_line = data.index('\n')

for ind in range(break_line-2, -1, -1):
    print(data[ind])
    for pos, val in enumerate(data[ind]):
        if ord(val) in range(ord('A'),ord('Z')+1):
            stacks[get_stack_index(pos)].push(val)


# ####### implement instrucitons - part 1
# for line in data[break_line+1:]:
#     line = line.rstrip('\n')
#     line = line.split(' ')
#     instruction = {}
#     for i, item in enumerate(line):
#         if i % 2 == 0:
#             instruction[item] = int(line[i+1])
    
#     for m in range(instruction['move']):
#         stack_val = stacks[instruction['from']].pop()
#         stacks[instruction['to']].push(stack_val)


####### implement instrucitons - part 2
for line in data[break_line+1:]:
    line = line.rstrip('\n')
    line = line.split(' ')
    instruction = {}
    for i, item in enumerate(line):
        if i % 2 == 0:
            instruction[item] = int(line[i+1])
    
    stack_vals = stacks[instruction['from']].pop_multiple(instruction['move'])
    stacks[instruction['to']].push_multiple(stack_vals)

    
####### print the result
for s in stacks.values():
    val = s.pop()
    print(val, end='')
    if val == ' ':
        continue
    s.push(val)

