def get_file_data(file_name):
    file_data = []
    try:
        with open(file_name, "r") as f:
            for line in f:
                line = line.strip()
                if line != "":
                    file_data.append(line)
    except FileNotFoundError:
        pass
    return file_data


def main(part_two=False):
    file_data = get_file_data("input_file")

    registers = {
        "a": 12,
        "b": 0,
        "c": 0,
        "d": 0
    }

    if part_two:
        registers['c'] = 1

    current_instruction = 0

    while current_instruction < len(file_data):
        instruction = file_data[current_instruction]
        parts = instruction.split(" ")
        instruction_name = parts[0]

        if instruction_name == "tgl":

            v = parts[1]
            if v.isalpha():
                value = registers[v]
            else:
                value = int(v)

            change_instruction_index = current_instruction + value
            if change_instruction_index >= len(file_data) or change_instruction_index < 0:
                current_instruction += 1
                continue
            else:
                instruction_to_change = file_data[change_instruction_index]
                change_parts = instruction_to_change.split(" ")
                if len(change_parts) == 2:

                    if "dec" in instruction_to_change:
                        instruction_to_change = instruction_to_change.replace("dec", "inc")
                        file_data[change_instruction_index] = instruction_to_change
                    elif "inc" in instruction_to_change:
                        instruction_to_change = instruction_to_change.replace("inc", "dec")
                        file_data[change_instruction_index] = instruction_to_change
                    elif "tgl" in instruction_to_change:
                        instruction_to_change = instruction_to_change.replace("tgl", "inc")
                        file_data[change_instruction_index] = instruction_to_change
                if len(change_parts) == 3:
                    if "jnz" in instruction_to_change:
                        instruction_to_change = instruction_to_change.replace("jnz", "cpy")
                        file_data[change_instruction_index] = instruction_to_change
                    elif "cpy" in instruction_to_change:
                        instruction_to_change = instruction_to_change.replace("cpy", "jnz")
                        file_data[change_instruction_index] = instruction_to_change

            current_instruction += 1
        elif instruction_name == "cpy":
            v = parts[1]
            if v.isalpha():
                value = registers[v]
            else:
                value = int(v)

            register = parts[2]
            if register.isnumeric():
                current_instruction += 1
                continue
            registers[register] = value
            current_instruction += 1

        elif instruction_name == "inc":
            register = parts[1]
            registers[register] += 1
            current_instruction += 1

        elif instruction_name == "dec":
            register = parts[1]
            registers[register] -= 1
            current_instruction += 1

        elif instruction_name == "jnz":
            v = parts[1]
            if v.isalpha():
                value = registers[v]
            else:
                value = int(v)

            if parts[2].isalpha():
                jump_value = registers[parts[2]]
            else:
                jump_value = int(parts[2])

            if value != 0:
                current_instruction += jump_value
            else:
                current_instruction += 1

    if not part_two:
        print("Part one answer:", registers['a'])


if __name__ == "__main__":
    main()


# I didn't do any optimization for Part 2. It took about ~30 minutes to finish
# but I got the right answer!
