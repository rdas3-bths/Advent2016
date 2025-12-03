from collections import deque
import hashlib

mvs = (('U', 0, -1), ('D', 0, 1), ('L', -1, 0), ('R', 1, 0))


def get_md5(str):
    md5_hash_object = hashlib.md5()
    md5_hash_object.update(str.encode('utf-8'))
    return md5_hash_object.hexdigest()


def open_doors(hash):
    available_moves = []
    for i in range(0, len(mvs)):
        if ord(hash[i]) > ord('a'):
            available_moves.append(mvs[i])
    return available_moves


def new_location(x, y, all_moves, mv):
    c, dx, dy = mv
    return x + dx, y + dy, all_moves + c


def in_bounds(x, y):
    return x >= 0 and x < 4 and y >= 0 and y < 4


def traverse_grid(inp, part):
    start_x = 0
    start_y = 0
    unvisited = [ (start_x, start_y, '') ]
    longest = 0
    while unvisited:
        x, y, all_moves = unvisited.pop(0)
        for mv in open_doors(get_md5(inp + all_moves)):
            new_x, new_y, new_all_moves = new_location(x, y, all_moves, mv)
            if not in_bounds(new_x, new_y):
                continue
            if new_x == 3 and new_y == 3:
                if part == 1:
                    return new_all_moves
                longest = len(new_all_moves)
            else:
                unvisited.append((new_x, new_y, new_all_moves))
    return longest


print(traverse_grid("qljzarfv", part=1))
print(traverse_grid("qljzarfv", part=2))
