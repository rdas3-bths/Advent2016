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


def new_location(row, col, all_moves, mv):
    direction, row_change, col_change = mv
    return row + row_change, col + col_change, all_moves + direction


def in_bounds(row, col):
    return row >= 0 and row < 4 and col >= 0 and col < 4


def traverse_grid(inp, part):
    start_row = 0
    start_col = 0
    unvisited = [ (start_row, start_col, '') ]
    longest = 0
    while unvisited:
        current_row, current_col, all_moves = unvisited.pop(0)
        for mv in open_doors(get_md5(inp + all_moves)):
            new_row, new_col, new_all_moves = new_location(current_row, current_col, all_moves, mv)
            if not in_bounds(new_row, new_col):
                continue
            if new_row == 3 and new_col == 3:
                if part == 1:
                    return new_all_moves
                longest = len(new_all_moves)
            else:
                unvisited.append((new_row, new_col, new_all_moves))
    return longest


print(traverse_grid("qljzarfv", part=1))
print(traverse_grid("qljzarfv", part=2))
