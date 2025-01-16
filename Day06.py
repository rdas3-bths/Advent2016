from advent_util import get_file_data
from collections import defaultdict

file_data = get_file_data("input_file")
character_map = {}

for i in range(len(file_data[0])):
    character_map[i] = defaultdict(int)
    for line in file_data:
        character_map[i][line[i]] += 1

part_one_answer = ""
part_two_answer = ""
for i in range(len(file_data[0])):
    part_one_answer += max(character_map[i], key = character_map[i].get)
    part_two_answer += min(character_map[i], key = character_map[i].get)

print("Part one answer:", part_one_answer)
print("Part two answer:", part_two_answer)