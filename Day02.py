from advent_util import get_file_data

data = get_file_data("input_file")
part_one_code = []
part_two_code = []
number = 5

PAD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
PAD2 = [
    ["X", "X", "1", "X", "X"],
    ["X", "2", "3", "4", "X"],
    ["5", "6", "7", "8", "9"],
    ["X", "A", "B", "C", "X"],
    ["X", "X", "D", "X", "X"]
]
part_one_row = 1
part_one_col = 1

part_two_row = 2
part_two_col = 0


for instructions in data:
    for instruction in instructions:

        # part one logic
        if instruction == "U" and part_one_row != 0:
            part_one_row -= 1
        if instruction == "D" and part_one_row != 2:
            part_one_row += 1
        if instruction == "L" and part_one_col != 0:
            part_one_col -= 1
        if instruction == "R" and part_one_col != 2:
            part_one_col += 1

        # part two logic
        if instruction == "U" and part_two_row != 0:
            if PAD2[part_two_row-1][part_two_col] != "X":
                part_two_row -= 1
        if instruction == "D" and part_two_row != 4:
            if PAD2[part_two_row+1][part_two_col] != "X":
                part_two_row += 1
        if instruction == "L" and part_two_col != 0:
            if PAD2[part_two_row][part_two_col-1] != "X":
                part_two_col -= 1
        if instruction == "R" and part_two_col != 4:
            if PAD2[part_two_row][part_two_col+1] != "X":
                part_two_col += 1

    part_one_code.append(PAD[part_one_row][part_one_col])
    part_two_code.append(PAD2[part_two_row][part_two_col])

print("Part one answer: ", end="")
for c in part_one_code:
    print(c, end="")

print()

print("Part two answer: ", end="")
for c in part_two_code:
    print(c, end="")

print()
