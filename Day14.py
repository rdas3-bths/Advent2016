import hashlib

all_hashes = {}

def get_md5(str):
    md5_hash_object = hashlib.md5()
    md5_hash_object.update(str.encode('utf-8'))
    return md5_hash_object.hexdigest()


def check_triple(str):
    i = 0
    while i < len(str)-2:
        current = str[i]
        next = str[i+1]
        third = str[i+2]
        if current == next and next == third:
            return True, current
        i += 1
    return False, ""


def check_five(str, char):
    i = 0
    while i < len(str)-4:
        first = str[i]
        second = str[i+1]
        third = str[i+2]
        fourth = str[i+3]
        fifth = str[i+4]
        if first == second == third == fourth == fifth == char:
            return True
        i += 1
    return False


def do_next_thousand(s, index, char):
    for i in range(0, 1000):
        salt = s + str(index)
        h = get_md5(salt)
        h = do_2016(h)
        if check_five(h, char):
            return True
        index += 1
    return False


def do_2016(h):
    original_hash = h
    if original_hash in all_hashes.keys():
        return all_hashes[original_hash]
    else:
        all_hashes[original_hash] = ""
    for i in range(0, 2016):
        h = get_md5(h)

    all_hashes[original_hash] = h
    return h

orig_salt = "yjdafjpo"
h = get_md5(orig_salt)
h = do_2016(h)

suffix = 0
counter = 0
key_number = 0
while True:
    salt = orig_salt + str(suffix)
    h = get_md5(salt)
    h = do_2016(h)
    result, char = check_triple(h)
    if result:
        five_check = do_next_thousand(orig_salt, suffix+1, char)
        if five_check:
            key_number += 1
    suffix += 1

    if key_number == 64:
        print("Part two answer", suffix-1)
        break