from advent_util import get_file_data

file_data = get_file_data("input_file")

rows = 25
cols = 37

grid = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append('.')
    grid.append(row)

nodes = []
for line in file_data:
    if "dev" in line:
        node = line.split()[0]
        node_x_value = int(node.split("-")[1][1:])
        node_y_value = int(node.split("-")[2][1:])
        used = int(line.split()[2][0:-1])
        avail = int(line.split()[3][0:-1])
        node_data = ((node_x_value, node_y_value), used, avail)
        nodes.append(node_data)

count = 0
for nodeA in nodes:
    if nodeA[1] != 0:
        for nodeB in nodes:
            if nodeA[0] != nodeB[0]:
                # if used nodeA can fit in avail nodeB
                nodeA_used = nodeA[1]
                nodeB_avail = nodeB[2]
                if nodeA_used <= nodeB_avail:
                    count += 1

print("Part one answer:", count)

for node in nodes:
    if node[1] == 0:
        node_location = node[0]
        node_row = node_location[1]
        node_col = node_location[0]
        grid[node_row][node_col] = '_'
    if node[1] > 100:
        node_location = node[0]
        node_row = node_location[1]
        node_col = node_location[0]
        grid[node_row][node_col] = '#'


for row in grid:
    print("".join(row))


    # 51 moves to get to next to top right
    # 1 move to put the _ at the top right, and G to the left of it
    # 5 * 35 moves to get G all the way to left
    # 51 + 1 + 175 = 227
    # 227 final answer, solved manually
    # used grid visual to help solve this
