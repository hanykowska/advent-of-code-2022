import numpy as np

f = open('2022-12-08.txt', 'r')
fe = open('2022-12-08-example.txt', 'r')

lines = f.readlines()

lines = [line.rstrip('\n') for line in lines]
trees = np.array([[int(t) for t in line] for line in lines])

print(trees)

trees_visibility = [[1 for t in line] for line in lines]
max_col = len(trees[0])-1
max_row = len(trees)-1
visible_count = 2*max_col + 2*max_row

for i in range(1,max_row):
    for j in range(1,max_col):
        # top:
        if max(trees[:i,j]) < trees[i,j]:
            trees_visibility[i][j] = 1
            visible_count += 1
            continue
        # left
        elif max(trees[i,:j]) < trees[i,j]:
            trees_visibility[i][j] = 1
            visible_count += 1
            continue
        # right
        elif max(trees[i,j+1:]) < trees[i,j]:
            trees_visibility[i][j] = 1
            visible_count += 1
            continue
        # bottom
        elif max(trees[i+1:,j]) < trees[i,j]:
            trees_visibility[i][j] = 1
            visible_count += 1
            continue
        else:
            trees_visibility[i][j] = 0

print(visible_count)
max_scenic_score = 0

# part 2
for i in range(1,max_row):
    for j in range(1,max_col):
        # if trees_visibility[i][j] == 1:
        #     continue
        current_score = 1
       
        arr = np.where(trees >= trees[i,j])

        # left, right
        arr_row = np.where(arr[0] == i)
        left = 0
        right = max_col
        for i_1, row in enumerate(arr_row[0]):
            curr_col = arr[1][row]
            if curr_col > left and curr_col < j:
                left = curr_col
            if curr_col > j:
                right = curr_col
                break
        current_score *= j-left
        current_score *= right-j

        # top, bottom
        arr_col = np.where(arr[1] == j)
        top = 0
        bottom = max_row
        for i_2, col in enumerate(arr_col[0]):
            curr_row = arr[0][col]
            if curr_row > top and curr_row < i:
                top = curr_row
            if curr_row > i:
                bottom = curr_row
                break
        current_score *= i-top
        current_score *= bottom-i

        if current_score > max_scenic_score:
            max_scenic_score = current_score

print(max_scenic_score)
