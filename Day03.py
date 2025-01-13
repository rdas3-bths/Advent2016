from advent_util import get_file_data


def check_triangle(triangle):
    sum1 = triangle[0] + triangle[1]
    sum2 = triangle[0] + triangle[2]
    sum3 = triangle[1] + triangle[2]

    is_triangle = True
    if sum1 <= triangle[2]:
        is_triangle = False
    if sum2 <= triangle[1]:
        is_triangle = False
    if sum3 <= triangle[0]:
        is_triangle = False

    return is_triangle


def get_sides_on_line(line):
    sides = line.split(" ")
    side_numbers = []
    for side in sides:
        if len(side) != 0:
            side_numbers.append(int(side))
    return side_numbers


file_data = get_file_data("input_file")

triangles_by_row = []

for line in file_data:
    triangles_by_row.append(get_sides_on_line(line))

triangles_by_column = []

i = 0
while i < len(file_data)-2:
    sides_line_one = get_sides_on_line(file_data[i])
    sides_line_two = get_sides_on_line(file_data[i+1])
    sides_line_three = get_sides_on_line(file_data[i+2])

    triangle1 = []
    triangle2 = []
    triangle3 = []

    triangle1.append(sides_line_one[0])
    triangle1.append(sides_line_two[0])
    triangle1.append(sides_line_three[0])

    triangle2.append(sides_line_one[1])
    triangle2.append(sides_line_two[1])
    triangle2.append(sides_line_three[1])

    triangle3.append(sides_line_one[2])
    triangle3.append(sides_line_two[2])
    triangle3.append(sides_line_three[2])

    triangles_by_column.append(triangle1)
    triangles_by_column.append(triangle2)
    triangles_by_column.append(triangle3)

    i += 3

part_one_answer = 0
for triangle in triangles_by_row:

    if check_triangle(triangle):
        part_one_answer += 1

print("Part one answer:", part_one_answer)

part_two_answer = 0
for triangle in triangles_by_column:

    if check_triangle(triangle):
        part_two_answer += 1

print("Part two answer:", part_two_answer)
