from advent_util import get_file_data

file_data = get_file_data("input_file")

GRID_HEIGHT=6
GRID_LENGTH=50

def make_rect(w, h, grid):
    for i in range(0, h):
        for j in range(0, w):
            grid[i][j] = "#"

def rotate_column(col, amount, grid):
    column_list = []
    for i in range(0, GRID_HEIGHT):
        column_list.append(grid[i][col])

    shifted_column_list = column_list[-amount:] + column_list[:-amount]

    for i in range(0, GRID_HEIGHT):
        grid[i][col] = shifted_column_list[i]

def rotate_row(row, amount, grid):
    row_list = []
    for i in range(0, GRID_LENGTH):
        row_list.append(grid[row][i])

    shifted_row_list = row_list[-amount:] + row_list[:-amount]

    for i in range(0, GRID_LENGTH):
        grid[row][i] = shifted_row_list[i]


def process_instructions(file_data, grid):
    for line in file_data:
        if "rect" in line:
            w = int(line.split(" ")[1].split("x")[0])
            h = int(line.split(" ")[1].split("x")[1])
            make_rect(w, h, grid)
        if "column" in line:
            # rotate column x=1 by 1
            col = int(line.split(" ")[2].split("=")[1])
            amount = int(line.split(" ")[4])
            rotate_column(col, amount, grid)
        if "row" in line:
            # rotate row y=0 by 4
            row = int(line.split(" ")[2].split("=")[1])
            amount = int(line.split(" ")[4])
            rotate_row(row, amount, grid)

grid = []

for i in range(0,GRID_HEIGHT):
    row = []
    for j in range(0,GRID_LENGTH):
        row.append('.')
    grid.append(row)

process_instructions(file_data, grid)

count = 0
for r in grid:
    for i in r:
        if i == "#":
            count += 1

print("Part one answer:", count)
print("Part two answer:")
for r in grid:
    for i in r:
        if i == "#":
            count += 1
        print(i, end="")
    print()


