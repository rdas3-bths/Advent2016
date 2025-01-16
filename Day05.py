import hashlib


part_one_password = ""
part_two_password = []
for i in range(8):
    part_two_password.append("-")

door_id = "cxdnnyjw"

code = 1
while len(part_one_password) != 8 or part_two_password.__contains__("-"):
    hash_input = door_id + str(code)
    hash = hashlib.md5(hash_input.encode())
    if hash.hexdigest().startswith("00000"):
        item = hash.hexdigest()[5]
        character = hash.hexdigest()[6]
        if item.isdigit():
            number = int(item)
            if 0 <= number <= 7:
                if part_two_password[number] == "-":
                    part_two_password[number] = character
        if len(part_one_password) != 8:
            part_one_password += item
    code += 1

print("Part one answer:", part_one_password)
print("Part two answer:", "".join(part_two_password))