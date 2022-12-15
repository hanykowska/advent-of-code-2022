fe = open('2022-12-07-example.txt','r')
f = open('2022-12-07.txt', 'r')

lines = f.readlines()

lines = [line.rstrip('\n') for line in lines]
print(len(lines))
print(len([line for line in lines if line.startswith('dir ')]))

# TODO: implement a tree class that has the following functions:
# - get current branch/node
# - add child node
# - change node
# - get node value (possibly a recurrent one as it would need to double-count the values)

class Node:
    def __init__(self, name='/', parent=None):
        self.name = name
        self.parent = parent
        self.child_values = []
        self.child_nodes = {}
        self.sum_of_total_values = 0
        self.sum_of_own_values = 0


    def add_child_node(self, child_name):
        self.child_nodes[child_name] = Node(child_name, self)
        self.sum_of_total_values = 0 #reset the total values once there's a child node added
        return self.child_nodes[child_name]

    def add_child_value(self, value):
        self.child_values.append(value)
        self.sum_of_own_values += value
        return None

    def sum_total_vals(self):
        if self.sum_of_total_values == 0:
            current_sum = sum(self.child_values)
            for ch_node in self.child_nodes:
                current_sum += self.child_nodes[ch_node].sum_total_vals()
            self.sum_of_total_values = current_sum

        return self.sum_of_total_values
    
    def get_child_total_vals(self, dir_list):
        if self.sum_of_total_values == 0:
            current_sum = sum(self.child_values)
            for ch_node in self.child_nodes:
                current_sum += self.child_nodes[ch_node].sum_total_vals()
            self.sum_of_total_values = current_sum
        for ch_node in self.child_nodes:
            dir_list.extend(self.child_nodes[ch_node].get_child_total_vals([]))
        dir_list.append(self.sum_of_total_values)
        return dir_list
    


size_p1_limit = 0
current_node = Node('/')
limit = 100000
dirs_calculated = set([])
dir_sizes = {}

for line in lines:
    if line.startswith('$ cd'):
        cwd = line.split(' ')[-1]
        if cwd == '..':
            # go one up
            curr_val_sum = current_node.sum_total_vals()
            dir_sizes[current_node.name] = curr_val_sum
            if curr_val_sum <= limit:
                size_p1_limit += curr_val_sum
                dirs_calculated.add(current_node.name)
            current_node = current_node.parent
        else:
            current_node = current_node.add_child_node(cwd)
    elif line[0].isdigit():
        current_node.add_child_value(int(line.split(' ')[0]))


# TODO: go through the tree upstream and recalculate the folders
while current_node.parent is not None:
    curr_val_sum = current_node.sum_total_vals()
    dir_sizes[current_node.name] = curr_val_sum
    if curr_val_sum <= limit and current_node.name not in dirs_calculated:
        size_p1_limit += curr_val_sum
        dirs_calculated.add(current_node.name)
    current_node = current_node.parent

dict_sizes = current_node.get_child_total_vals([])

print(size_p1_limit)
print(len(dir_sizes))
# part 2
space_needed = 30000000 - (70000000 - max(dir_sizes.values()))

print(min(val for val in dict_sizes if val >= space_needed))