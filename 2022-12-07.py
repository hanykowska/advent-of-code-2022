fe = open('2022-12-07-example.txt','r')

lines = fe.readlines()

lines = [line.rstrip('\n') for line in lines]

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
        if self.sum_of_values == 0:
            current_sum = sum(self.child_values)
            for ch_node in self.child_nodes:
                current_sum += ch_node.sum_vals()
            self.sum_of_values = current_sum

        return self.sum_of_values

    


size_p1_limit = 0
current_node = Node('/')
limit = 100000

for line in lines:
    if line.startswith('$ cd'):
        cwd = line.split(' ')[-1]
        if cwd == '..':
            # go one up
            curr_val_sum = current_node.sum_total_values()
            if curr_val_sum <= limit:
                size_p1_limit += curr_val_sum
            current_node = current_node.parent
        else:
            current_node = current_node.add_child_node(cwd, current_node)
    elif isdigit(line[0]):
        current_node.add_child_value(int(line.split(' ')[0]))


# TODO: go through the tree upstream and recalculate the folders
