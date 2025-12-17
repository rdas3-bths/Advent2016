from advent_util import get_file_data

file_data = get_file_data("input_file")

nodes = []
for line in file_data:
    if "dev" in line:
        node = line.split()[0]
        used = int(line.split()[2][0:-1])
        avail = int(line.split()[3][0:-1])
        node_data = (node, used, avail)
        nodes.append(node_data)

count = 0
for nodeA in nodes:
    if nodeA[1] != 0:
        for nodeB in nodes:
            if nodeA[0] != nodeB[0]:
                # if used nodeA can fit in avail nodeB
                nodeA_used = nodeA[1]
                nodeB_avail = nodeB[2]
                if nodeA_used <= nodeB_avail:
                    count += 1

print("Part one answer:", count)

