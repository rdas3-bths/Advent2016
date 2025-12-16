from advent_util import get_file_data
import itertools

part_one_password = "abcdefgh"
part_two_password = "fbgdceah"
password = [letter for letter in part_one_password]


def swap_by_index(x, y, password):
    temp = password[x]
    password[x] = password[y]
    password[y] = temp
    return password


def swap_by_letter(x, y, password):
    index_x = password.index(x)
    index_y = password.index(y)
    swap_by_index(index_x, index_y, password)
    return password


def rotate_once(password, direction):
    password_new = []
    if direction == "right":
        i = len(password)-1
    else:
        i = 1
    count = 0
    while count < len(password):
        letter = password[i]
        password_new.append(letter)
        i += 1
        count += 1
        if i == len(password):
            i = 0

    return password_new



def rotate_password(steps, password, direction, reverse=False):

    if reverse:
        if direction == "right":
            direction = "left"
        else:
            direction = "right"

    for i in range(steps):
        password = rotate_once(password, direction)

    return password


def rotate_by_letter(password, letter, reverse=False):
    index_of_letter = password.index(letter)
    amount = 1 + index_of_letter
    if index_of_letter >= 4:
        amount += 1

    if reverse:
        return rotate_password(amount, password, "left")
    else:
        return rotate_password(amount, password, "right")


def reverse_password(password, start, end):
    reversed_portion = []
    for i in range(start, end+1):
        reversed_portion.append(password[i])

    reversed_portion.reverse()

    before = []
    for i in range(0, start):
        before.append(password[i])

    after = []
    for i in range(end+1, len(password)):
        after.append(password[i])

    return before + reversed_portion + after


def move_letter(password, source, destination, reverse=False):

    if reverse:
        temp = source
        source = destination
        destination = temp

    removed = password.pop(source)
    password.insert(destination, removed)
    return password


def process_instruction(password, instruction, reverse=False):
    instructions_processed = 0
    if "rotate right" in instruction:
        instructions_processed += 1
        steps = int(instruction.split(" ")[2])
        password = rotate_password(steps, password, "right", reverse)

    elif "rotate left" in instruction:
        instructions_processed += 1
        steps = int(instruction.split(" ")[2])
        password = rotate_password(steps, password, "left", reverse)

    # swap position 2 with position 4
    elif "swap position" in instruction:
        instructions_processed += 1
        x = int(instruction.split(" ")[2])
        y = int(instruction.split(" ")[5])
        password = swap_by_index(x, y, password)

    # swap letter h with letter a
    elif "swap letter" in instruction:
        instructions_processed += 1
        letter_one = instruction.split(" ")[2]
        letter_two = instruction.split(" ")[5]
        password = swap_by_letter(letter_one, letter_two, password)

    # rotate based on position of letter g
    elif "rotate based" in instruction:
        instructions_processed += 1
        letter = instruction.split(" ")[6]
        password = rotate_by_letter(password, letter, reverse)

    # reverse positions 2 through 4
    elif "reverse" in instruction:
        instructions_processed += 1
        start = int(instruction.split(" ")[2])
        end = int(instruction.split(" ")[4])
        password = reverse_password(password, start, end)

    # move position 6 to position 0
    elif "move" in instruction:
        source = int(instruction.split(" ")[2])
        destination = int(instruction.split(" ")[5])
        password = move_letter(password, source, destination, reverse)



    return password


def scramble_word(pw, instructions):
    for line in instructions:
        pw = process_instruction(pw, line)

    return pw

file_data = get_file_data("input_file")

pw = scramble_word(password, file_data)

print("Part one answer:", "".join(pw))

all_perms = [''.join(s) for s in itertools.permutations(part_one_password)]

for passwd in all_perms:
    result = scramble_word(passwd, file_data)
    result_string = "".join(result)
    if result_string == part_two_password:
        print("Part two answer:", passwd)

