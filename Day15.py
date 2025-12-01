discs = {}

discs["1"] = [5, 2]
discs["2"] = [13, 7]
discs["3"] = [17, 10]
discs["4"] = [3, 2]
discs["5"] = [19, 9]
discs["6"] = [7, 0]
discs["7"] = [11, 0]


def get_position(disc, time):
    return (discs[disc][1] + time) % discs[disc][0]


def do_capsule(available_discs):

    initial_start_time = 0
    while True:
        success = True
        current_time = initial_start_time
        for disc in available_discs:
            current_time += 1
            position = get_position(disc, current_time)
            if position != 0:
                success = False

        initial_start_time += 1
        if success:
            if len(available_discs) == 6:
                print("Part one answer:", initial_start_time)
            else:
                print("Part two answer:", initial_start_time)
            break


do_capsule("123456")
do_capsule("1234567")
