
# a new tile is a trap if:
# Its left and center tiles are traps, but its right tile is not.
# Its center and right tiles are traps, but its left tile is not.
# Only its left tile is a trap.
# Only its right tile is a trap.

def get_next_row(current_row):
    next_row = []
    for i in range(len(current_row)):
        new_tile = ""
        center=current_row[i]

        if i == 0:
            left="."
        else:
            left=current_row[i-1]

        if i == len(current_row)-1:
            right="."
        else:
            right=current_row[i+1]

        if left == "^" and center == "^" and right == ".":
            new_tile = "^"

        elif center == "^" and right == "^" and left == ".":
            new_tile = "^"

        elif left == "^" and center == "." and right == ".":
            new_tile = "^"

        elif right == "^" and center == "." and left == ".":
            new_tile = "^"

        else:
            new_tile = "."

        next_row.append(new_tile)

    return next_row

all_rows = []
starting_row = ".^..^....^....^^.^^.^.^^.^.....^.^..^...^^^^^^.^^^^.^.^^^^^^^.^^^^^..^.^^^.^^..^.^^.^....^.^...^^.^."
current_row = starting_row
all_rows.append(starting_row)
for i in range(0, 399999):
    next_row = get_next_row(current_row)
    all_rows.append(next_row)
    current_row = next_row

part_one_answer = 0
for row in all_rows:
    for letter in row:
        if letter == ".":
            part_one_answer += 1


print("Part one answer:", part_one_answer)