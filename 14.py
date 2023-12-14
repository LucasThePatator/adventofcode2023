import numpy as np
from tqdm import trange

def parse_file(data):
    lines = data.split('\n')
    platform = np.empty((len(lines), len(lines[0])), dtype=np.uint8)
    for row, line in enumerate(lines):
        temp = list(map(lambda c : {'.' : 0, '#' : 1, 'O' : 2}[c], line))
        platform[row, :]  = np.array(temp)

    return platform

def tilt_platform(platform):
    blockers = np.zeros((platform.shape[1]), dtype=np.uint8)
    for row in range(platform.shape[0]):
        current_row = platform[row, :]
        for loc in range(platform.shape[1]):
            if current_row[loc] == 1:
                blockers[loc] = row + 1
            if current_row[loc] == 2:
                current_row[loc] = 0
                platform[blockers[loc], loc] = 2
                blockers[loc] += 1

    return platform

def print_platform(platform):
    for row in platform:
        print( "".join(map(lambda c : {0 : '.', 1 : '#' , 2 : 'O'}[c], row)))

def hash_array(array : np.ndarray):
    value = hash(array.data.tobytes())
    return value

class Tumbler:
    def __init__(self):
        self.cache = {}

    def cycle(self, platform):
        current_hash = hash_array(platform)
        if current_hash in self.cache.keys():
            return True, self.cache[current_hash]

        platform = tilt_platform(platform)
        platform = np.rot90(platform, axes=(1, 0))
        platform = tilt_platform(platform)
        platform = np.rot90(platform, axes=(1, 0))
        platform = tilt_platform(platform)
        platform = np.rot90(platform, axes=(1, 0))
        platform = tilt_platform(platform)
        platform = np.rot90(platform, axes=(1, 0))

        self.cache[current_hash] = platform.copy()

        return False, platform

def count_load(platform):
    rows_count = np.sum(platform == 2, axis=1)
    weights = np.arange(platform.shape[0], 0, -1)
    return sum(rows_count * weights)


def main():
    with open('./data/14', 'r') as data_file:
        platform = parse_file(data_file.read())

    tumbler = Tumbler()

    for i in trange(1_000_000_000):
        res, platform = tumbler.cycle(platform)

        if res:
            break
    
    stop_index = i
    og_platform = platform.copy()
    counts = []

    _, platform = tumbler.cycle(platform)
    counts.append(count_load(platform))
    while (platform != og_platform).any():
        _, platform = tumbler.cycle(platform)
        counts.append(count_load(platform))
    
    nb_counts = len(counts)
    index = (1_000_000_000 - stop_index - 2) % nb_counts

    print(counts[index])
if __name__ == "__main__":
    main()