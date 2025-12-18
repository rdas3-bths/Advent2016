from advent_util import get_file_data
import itertools

file_data = get_file_data("input_file")

grid = []
number_map = {}

row_num = 0
col_num = 0
numbers_in_grid = []
for line in file_data:
    row = []
    col_num = 0
    for letter in line:
        if letter.isnumeric():
            number_map[letter] = (row_num, col_num)
            numbers_in_grid.append(int(letter))
            row.append('.')
        else:
            row.append(letter)

        col_num += 1
    grid.append(row)
    row_num += 1

rows = len(grid)
columns = len(grid[0])
numbers_in_grid = sorted(numbers_in_grid)


def traverse_maze(grid, start, end):
    steps_to_goal = []
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

    return steps_to_goal


def find_distances(distances, part_two=False):
    all_distances = []
    for combo in combinations:
        full_combo = "0" + combo
        if part_two:
            full_combo += "0"
        distance = 0
        for i in range(len(full_combo) - 1):
            first = full_combo[i]
            second = full_combo[i + 1]
            path = (int(first), int(second))
            step_distance = distances[path]
            distance += step_distance
        all_distances.append(distance)
    return all_distances

distances = {}

for i in range(0, len(numbers_in_grid)):
    for j in range(0, len(numbers_in_grid)):
        if i != j:
            start = number_map[str(i)]
            end = number_map[str(j)]
            results = traverse_maze(grid, start, end)
            min_steps = min(results)
            distances[(i, j)] = min_steps

s = ""
for i in range(1, len(numbers_in_grid)):
    s += str(numbers_in_grid[i])

perms = itertools.permutations(s)
combinations = [''.join(p) for p in perms]

all_distances = find_distances(distances)
print("Part one answer:", min(all_distances))

all_distances = find_distances(distances, True)
print("Part two answer:", min(all_distances))
