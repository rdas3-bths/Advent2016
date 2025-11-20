from advent_util import get_file_data

configuration = {}

def check_bot_configuration(confiuration):
    for key in configuration.keys():
        chips = configuration[key]
        if 17 in chips and 61 in chips:
            print("Part one answer:", key.split(" ")[1])


def set_initial_chips(file_data):

    for line in file_data:
        if line.startswith("value"):
            chip_value = int(line.split(" ")[1])
            bot_number = "bot " + line.split(" ")[5]
            if bot_number in configuration.keys():
                configuration[bot_number].append(chip_value)
            else:
                configuration[bot_number] = [chip_value]

    return configuration


def set_chips(file_data, configuration):

    while len(file_data) != 0:
        check_bot_configuration(configuration)
        for line in file_data:
            if "value" in line:
                chip_value = int(line.split(" ")[1])
                bot_number = "bot " + line.split(" ")[5]
                if bot_number in configuration.keys():
                    configuration[bot_number].append(chip_value)
                else:
                    configuration[bot_number] = [chip_value]
                file_data.remove(line)
                break
            if "give" in line:
                sender = line.split(" ")[0] + " " + line.split(" ")[1]
                if not sender in configuration.keys():
                    continue
                else:
                    if len(configuration[sender]) != 2:
                        continue

                low_receiver = line.split(" ")[5] + " " + line.split(" ")[6]
                high_receiver = line.split(" ")[10] + " " + line.split(" ")[11]

                low_chip = min(configuration[sender])
                high_chip = max(configuration[sender])

                configuration[sender] = []

                if low_receiver in configuration.keys():
                    configuration[low_receiver].append(low_chip)
                else:
                    configuration[low_receiver] = [low_chip]

                if high_receiver in configuration.keys():
                    configuration[high_receiver].append(high_chip)
                else:
                    configuration[high_receiver] = [high_chip]

                file_data.remove(line)

file_data = get_file_data("input_file")
set_chips(file_data, configuration)
print("Part two answer:", configuration["output 0"][0] * configuration["output 1"][0] * configuration["output 2"][0])