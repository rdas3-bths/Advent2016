from advent_util import get_file_data

file_data = get_file_data("input_file")


def is_in_range(number, ranges):
    for range in ranges:
        if number >= range[0] and number <= range[1]:
            return True

    return False

ranges = []

for line in file_data:
    minimum = int(line.split("-")[0])
    maximum = int(line.split("-")[1])
    ranges.append([minimum, maximum])

ranges = sorted(ranges, key=lambda list: list[0])

for num in range(0, 4294967296):
    if not is_in_range(num, ranges):
        print("Part one answer:", num)
        break

i = 0
while i < len(ranges) - 1:
    if ranges[i][1] >= ranges[i + 1][0] - 1:
        ranges[i][1] = max(ranges[i][1], ranges[i + 1][1])
        ranges.pop(i + 1)
    else:
        i += 1

allowed = 4294967296
for range in ranges:
    min = range[0]
    max = range[1]
    allowed -= (max - min) + 1

print("Part two answer:", allowed)