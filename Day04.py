from advent_util import get_file_data


def generate_code(name):
    code = []
    for letter in set(name):
        code.append((-name.count(letter), letter))

    sorted_code = sorted(code)
    real_code = ""
    for i in range(5):
        real_code += sorted_code[i][1]
    return real_code


file_data = get_file_data("input_file")

rooms = []

for line in file_data:
    room = {}
    room_data = line.split("[")[0].split("-")
    room_code = line.split("[")[1][:-1]
    room_name = ""
    for i in range(len(room_data)-1):
        room_name += room_data[i]
    room["name"] = room_name
    room["id"] = int(room_data[len(room_data)-1])
    room["code"] = room_code
    rooms.append(room)

part_one_answer = 0
part_two_answer = 0
for room in rooms:
    occurrences = []
    for char in room["code"]:
        occurrences.append(room["name"].count(char))
    if generate_code(room["name"]) == room["code"]:
        part_one_answer += room["id"]
        decrypted_name = ""
        for letter in room["name"]:
            new_letter = chr((ord(letter) - 97 + room["id"]) % 26 + 97)
            decrypted_name += new_letter
        if decrypted_name == "northpoleobjectstorage":
            part_two_answer = room["id"]

print("Part one answer:", part_one_answer)
print("Part two answer:", part_two_answer)