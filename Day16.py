PART_ONE_LENGTH = 272
PART_TWO_LENGTH = 35651584
INPUT = "01000100010010111"


def do_dragon_curve(a):
    b = a
    b = b[::-1]
    new_b = ""

    for letter in b:
        if letter == "0":
            new_b += "1"
        if letter == "1":
            new_b += "0"

    b = new_b

    result = a + "0" + b
    return result


def get_check_sum(result):
    check_sum = []
    i = 0
    while i < len(result)-1:
        current = result[i]
        next = result[i+1]

        if current == next:
            check_sum.append("1")
        else:
            check_sum.append("0")

        i += 2

    return check_sum


def get_correct_check_sum(string):
    check_sum = string
    while True:
        check_sum = get_check_sum(check_sum)
        if len(check_sum) % 2 == 1:
            return check_sum


def get_dragon_curve_given_length(string, length):
    result = string
    while True:
        result = do_dragon_curve(result)
        if len(result) >= length:
            return result[0:length]


dragon_curve = get_dragon_curve_given_length(INPUT, PART_ONE_LENGTH)
result = get_correct_check_sum(dragon_curve)
print("Part one answer:", ''.join(result))

dragon_curve = get_dragon_curve_given_length(INPUT, PART_TWO_LENGTH)
result = get_correct_check_sum(dragon_curve)
print("Part two answer:", ''.join(result))