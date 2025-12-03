fav_number = 1350
rows = 50
columns = 50

def traverse_maze(grid):
    steps_to_goal = []
    start = (1, 1)
    end = (rows, columns)
    #                  r        d        l        u
    direction_map = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    visited = {}

    unvisited = [(start, 0, 0)]
    while unvisited:
        (current_row, current_col), curr_score, curr_dir = unvisited.pop(0)
        if (current_row, current_col) == end:
            steps_to_goal.append(curr_score)

        if ((current_row, current_col), curr_dir) in visited:
            continue

        visited[((current_row, current_col), curr_dir)] = curr_score

        for dir_index, (row_change, col_change) in enumerate(direction_map):

            new_row, new_col = current_row + row_change, current_col + col_change

            if (curr_dir + 2) % 4 == dir_index:
                continue
            if new_row > rows-1:
                continue
            if new_col > columns-1:
                continue
            if new_row < 0:
                continue
            if new_col < 0:
                continue

            if grid[new_row][new_col] != "#":
                unvisited.append(((new_row, new_col), curr_score + 1, dir_index))

    return visited

def count_ones(binary_value):
    count = 0
    for letter in binary_value:
        if letter == "1":
            count += 1
    return count


def open_or_wall(x, y):
    value = x * x + 3 * x + 2 * x * y + y + y * y
    value += fav_number
    binary_value = str(bin(value))[2:]
    ones = count_ones(binary_value)
    if ones % 2 == 0:
        return True
    else:
        return False

grid = []

for y in range(0, rows):
    row = []
    for x in range(0, columns):
        if open_or_wall(x, y):
            row.append(".")
        else:
            row.append("#")
    grid.append(row)

nodes = traverse_maze(grid)

for n in nodes:
    point = n[0]
    if point == (39, 31):
        print("Part one answer:", nodes[n])

points = []
for n in nodes:
    if nodes[n] <= 50:
        points.append(n[0])

unique_points = set(points)

print("Part two answer:", len(unique_points))