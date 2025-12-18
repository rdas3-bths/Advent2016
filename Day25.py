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


def main(a):
    file_data = get_file_data("input_file")

    output = ""
    counter = 0

    registers = {
        "a": a,
        "b": 0,
        "c": 0,
        "d": 0
    }

    current_instruction = 0

    while current_instruction < len(file_data):
        instruction = file_data[current_instruction]
        parts = instruction.split(" ")
        instruction_name = parts[0]

        if instruction_name == "cpy":
            v = parts[1]
            if v.isalpha():
                value = registers[v]
            else:
                value = int(v)

            register = parts[2]
            if register.isnumeric():
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

        elif instruction_name == "out":
            value = registers[parts[1]]
            output += str(value)
            current_instruction += 1
            counter += 1

        elif instruction_name == "jnz":
            v = parts[1]
            if v.isalpha():
                value = registers[v]
            else:
                value = int(v)

            jump_value = int(parts[2])

            if value != 0:
                current_instruction += jump_value
            else:
                current_instruction += 1

        if counter == 16:
            return output
            break


if __name__ == "__main__":
    a = 0
    while True:
        output = main(a)
        if output == "0101010101010101":
            print("Part one answer:", a)
            break
        a += 1
