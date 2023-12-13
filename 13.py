import numpy as np
from functools import reduce
import time

def parse_file(data_file):
    blocks_strings = data_file.read().split('\n\n')
    maps = []
    for block_str in blocks_strings:
        lines = block_str.split('\n')
        current_map = np.empty((len(lines), len(lines[0])))
        for row, line in enumerate(lines):
            current_row =  list(map(lambda c : {'.' : 0, '#' : 1}[c], line))
            current_map[row] = np.array(current_row)

        maps.append(current_map)
    
    return maps

def get_smudges(current_map):
    smudges = []
    for row_i in range(current_map.shape[0]):
        for col_i in range(current_map.shape[1]):
            new_map = np.copy(current_map)
            new_map[row_i, col_i] = 1 - current_map[row_i, col_i]
            smudges.append(new_map)

    return smudges


def find_offset(current_map):
    offsets = set()
    for i in range(1, current_map.shape[0] // 2 + 1 ):
        if (current_map[0:i,:] == np.flip(current_map[i:2*i,:],axis=0)).all():
            offsets.add(100*i)

    for i in range(current_map.shape[0] // 2 + 1, current_map.shape[0] ):
        if (current_map[2*i - current_map.shape[0]:i,:] == np.flip(current_map[i:,:], axis=0)).all():
            offsets.add(100*i)

    for i in range(1, current_map.shape[1] // 2 + 1):
        if (current_map[:,0:i] == np.flip(current_map[:,i:2*i], axis=1)).all():
            offsets.add(i)

    for i in range(current_map.shape[1] // 2 + 1, current_map.shape[1] ):
        if (current_map[:,2*i - current_map.shape[1]:i] == np.flip(current_map[:,i:], axis=1)).all():
            offsets.add(i)

    return offsets

def main():
    with open('./data/13', 'r') as data_file:
        data = parse_file(data_file)

    original_values = []
    start_time = time.perf_counter()
    total_sum = 0
    for d in data:
        value = list(find_offset(d))[0]
        original_values.append(value)
        total_sum += value
    end_time = time.perf_counter()

    print(total_sum)
    print(f"finished in {end_time-start_time}s")

    start_time = time.perf_counter()
    total_sum = 0
    for i, (d, og) in enumerate(zip(data, original_values)):
        for s in get_smudges(d):
            res = find_offset(s)
            res = res.difference(set([og]))
            if len(res) > 0:
                total_sum += list(res)[0]
                break
        else:
            print(i)
    print(total_sum)
    end_time = time.perf_counter()

    print(f"finished in {end_time-start_time}s")

if __name__ == "__main__":
    main()
