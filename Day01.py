def get_new_direction(direction, turn):
    if direction == "N":
        if turn == "R":
            return "E"
        if turn == "L":
            return "W"

    if direction == "E":
        if turn == "R":
            return "S"
        if turn == "L":
            return "N"

    if direction == "W":
        if turn == "R":
            return "N"
        if turn == "L":
            return "S"

    if direction == "S":
        if turn == "R":
            return "W"
        if turn == "L":
            return "E"

    return direction


directions = "L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4"
directions = directions.split(",")
for i in range(len(directions)):
    directions[i] = directions[i].strip()

current_direction = "N"
start_x = 0
start_y = 0
visited = []
visit_again = False

for d in directions:
    turn = d[0]
    moves = int(d[1:])

    current_direction = get_new_direction(current_direction, turn)
    if current_direction == "N":
        for i in range(moves):
            if (start_x, start_y) in visited:
                print("Visited again", start_x, start_y)
                visit_again = True
                break
            visited.append((start_x, start_y))
            start_y += 1
    if current_direction == "S":
        for i in range(moves):
            if (start_x, start_y) in visited:
                print("Visited again", start_x, start_y)
                visit_again = True
                break
            visited.append((start_x, start_y))
            start_y -= 1
    if current_direction == "E":
        for i in range(moves):
            if (start_x, start_y) in visited:
                print("Visited again", start_x, start_y)
                visit_again = True
                break
            visited.append((start_x, start_y))
            start_x += 1
    if current_direction == "W":
        for i in range(moves):
            if (start_x, start_y) in visited:
                print("Visited again", start_x, start_y)
                visit_again = True
                break
            visited.append((start_x, start_y))
            start_x -= 1

    if visit_again:
        break

print("Position:", start_x, start_y)
print("Distance:", abs(start_x) + abs(start_y))
print(visited)
