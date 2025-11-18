from advent_util import get_file_data


def check_abba(data):
    for i in range(len(data)):
        check_string = data[i:i+4]
        if len(check_string) == 4:
            if check_string[0] != check_string[1]:
                if (check_string[0] + check_string[1]) == (check_string[3] + check_string[2]):
                    return True
    return False


def check_aba(data):
    check_strings = []
    for i in range(len(data)):
        check_string = data[i:i+3]
        if len(check_string) == 3:
            if check_string[0] != check_string[1]:
                if check_string[0] == check_string[2]:
                    check_strings.append(check_string)
    return check_strings



file_data = get_file_data("input_file")

ip_data = []
for line in file_data:
    all_out_brackets = []
    all_in_brackets = []
    out_brackets = ""
    in_brackets = ""
    currently_in_bracket = False
    for i in range(len(line)):
        current_char = line[i]
        if not currently_in_bracket and line[i] != "[" and line[i] != "]":
            out_brackets += line[i]
        if currently_in_bracket and line[i] != "[" and line[i] != "]":
            in_brackets += line[i]
        if line[i] == "[":
            all_out_brackets.append(out_brackets)
            out_brackets = ""
            currently_in_bracket = True
        if line[i] == "]":
            all_in_brackets.append(in_brackets)
            in_brackets = ""
            currently_in_bracket = False
        if i == len(line)-1:
            all_out_brackets.append(out_brackets)

    ip_data.append((all_out_brackets, all_in_brackets))

part_one_answer = 0

for ip in ip_data:
    found_abba_inside = False
    found_abba_outside = False
    for outside in ip[0]:
        if check_abba(outside):
            found_abba_outside = True
    for inside in ip[1]:
        if check_abba(inside):
            found_abba_inside = True
    if found_abba_outside and not found_abba_inside:
        part_one_answer += 1

part_two_answer = 0
for ip in ip_data:
    found_aba_bab = False
    for outside in ip[0]:
        check_strings = check_aba(outside)
        if len(check_strings) != 0:
            for check_string in check_strings:
                bab = check_string[1] + check_string[0] + check_string[1]
                for inside in ip[1]:
                    if inside.__contains__(bab):
                        found_aba_bab = True
    if found_aba_bab:
        part_two_answer += 1


print("Part one answer:", part_one_answer)
print("Part two answer:", part_two_answer)