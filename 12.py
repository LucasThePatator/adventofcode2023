import numpy as np
from tqdm import tqdm
from functools import cache
from multiprocessing import Pool

def parse_line(line :  str):
    arrangements, groups = line.split(' ')
    groups = tuple(map(int, groups.split(',')))
    return arrangements, groups

def convert_arrangement(arrangement : str):
    temp = list(map(lambda c : {'.' : 0, '#' : 2, '?' : 1}[c], arrangement))
    return np.array(temp)

@cache
def compute_arrangements(arrangement : str, groups):
    arr = convert_arrangement(arrangement)
    if len(groups) == 0:
        if arr.shape[0] > 0 and arr.max() < 2:
            return 1
        if arr.shape[0] == 0:
            return 1
        return 0

    total_size = sum(groups)+len(groups) - 1
    if total_size > arr.shape[0]:
        return 0

    total = 0
    size = groups[0]
    local_array = np.ones(size)
    for i in range(arr.shape[0] - total_size + 1):
        if i > 0 and arr[0:i].max() == 2:
            continue
        if i + size < arr.shape[0] and arr[i+size] == 2:
            continue
        if (arr[i:i+size] - local_array).min() < 0:
            continue

        total += compute_arrangements(arrangement[i+size+1:], groups[1:])

    return total

def unfold(arrangement, groups):
    arrangement = "?".join([arrangement]*5)
    groups = groups*5
    return arrangement, groups

def process(line : str):
    arrangement, groups = parse_line(line)
    arrangement, groups = unfold(arrangement, groups)
    value = compute_arrangements(arrangement, groups)
    return value

def main():
    with open("./data/12", 'r') as data_file:
        total_sum = 0
        for line in data_file:
            arrangement, groups = parse_line(line)
            value = compute_arrangements(arrangement, groups)
            total_sum += value

        print(total_sum)

    with open("./data/12", 'r') as data_file:
        lines = data_file.read().split('\n')
        total_sum = 0
        with Pool(processes=10) as p:
            for v in tqdm(p.imap_unordered(process, lines, chunksize=20), total = len(lines)):
                total_sum += v
        
        print(total_sum)


if __name__ == "__main__":
    main()