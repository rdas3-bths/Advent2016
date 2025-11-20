from advent_util import get_file_data

string = get_file_data("input_file")[0]



def do_part_one(string):

    weights = []
    letters = []

    for letter in string:
        weights.append(0)
        letters.append(letter)

    processing_marker = False
    i = 0
    while i < len(letters):
        current_letter = letters[i]
        if not processing_marker:
            if current_letter != "(":
                weights[i] += 1
            else:
                processing_marker = True

        if processing_marker:
            marker = ""
            j = i + 1

            while letters[j] != ")":
                marker += letters[j]
                j += 1

            chars = int(marker.split("x")[0])
            amount = int(marker.split("x")[1])
            position = j+1
            for i in range(0, chars):
                weights[position] += amount
                position += 1
                j += 1
            processing_marker = False
            i = j

        i += 1

    return weights, letters


def do_part_two(string):
    weights = []
    letters = []
    answer = 0

    for letter in string:
        weights.append(1)
        letters.append(letter)

    i = 0
    while i < len(letters):
        letter = letters[i]
        if letter.isupper():
            answer += weights[i]
        elif letter == '(':
            marker = ""
            j = i + 1
            while letters[j] != ")":
                marker += letters[j]
                j += 1
            chars = int(marker.split("x")[0])
            amount = int(marker.split("x")[1])
            j += 1
            for x in range(0, chars):
                weights[j] *= amount
                j += 1
        i += 1

    return answer



weights1, letters1 = do_part_one(string)
print("Part one answer:", sum(weights1))
print("Part two answer:", do_part_two(string))
