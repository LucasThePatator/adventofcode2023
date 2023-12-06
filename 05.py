from tqdm import tqdm
import time

def parse_file(data_file : str):
    blocks = data_file.split('\n\n')
    seeds = list(map(int, blocks[0].split(": ")[1].split(' ')))

    maps = []
    for block in blocks[1:]:
        current_map = []
        ranges = block.split('\n')[1:]
        for r in ranges:
            start_dest, start_src, length = list(map(int, r.split(' ')))
            current_map.append((start_dest, start_src, length))

        maps.append(current_map)

    return seeds, maps
    
def get_seed_location(seed : int, maps):
    current_value = seed
    for m in maps:
        for r in m:
            if r[1] <= current_value <= (r[1] + r[2]):
                current_value = r[0] + current_value - r[1]
                break

    return current_value

def get_next_ranges(seed_range, local_map):
    remain_ranges = []
    new_seed_range = None
    r = local_map
    has_hit = False
    if seed_range[0] >= r[1] and seed_range[0] < r[1] + r[2]: #The start of the seed range is in the map range
        has_hit = True
        new_seed_range = [r[0] + seed_range[0] - r[1], -1]
        if seed_range[1] < r[1] + r[2]: #The seed range is completely in the map range
            new_seed_range[1] = r[0] + seed_range[1] - r[1]
        else : #The seed range goes outside the map range
            new_seed_range[1] = r[2] + r[0] - 1
            remain_ranges.append([r[1] + r[2], seed_range[1]])
    elif seed_range[1] < r[1] + r[2] and seed_range[1] >= r[1]: #The end of the seed range is in the map range, the start is not at this point
        has_hit = True
        new_seed_range = [r[0],  r[0] + seed_range[1] - r[1]]
        remain_ranges.append([seed_range[0], r[1] - 1])
    elif seed_range[0] < r[1] and seed_range[1] >= r[1] + r[2]: #there's map range in the middle
        has_hit = True
        new_seed_range = [r[0],  r[0] + r[2] - 1]
        remain_ranges.append([seed_range[0], r[1] - 1]) #before
        remain_ranges.append([r[1] + r[2], seed_range[1]])

    return has_hit, remain_ranges, new_seed_range


if __name__ == "__main__":
    seeds, maps = None, None

    with open('./data/05', 'r') as data_file:
        seeds, maps = parse_file(data_file.read())

    locations = []
    for seed in seeds:
        location = get_seed_location(seed, maps)
        locations.append(location)

    print(min(locations))

    current_ranges = []
    for i in range(0, len(seeds), 2):
        current_ranges.append([seeds[i], seeds[i] + seeds[i+1] - 1])

    print(current_ranges)

    start_time = time.perf_counter()
    for current_map in tqdm(maps):
        output_ranges = []
        while len(current_ranges) > 0:
            current_range = current_ranges.pop(0)
            has_hit = False
            for local_map in current_map:
                has_hit, remaining, new_range = get_next_ranges(current_range, local_map)
                if has_hit:
                    output_ranges.append(new_range)
                    if len(remaining) > 0:
                        current_ranges.extend(remaining)
                    break
            if not has_hit:
                output_ranges.append(current_range)

        current_ranges = output_ranges

    min_value = 2**63
    for r in current_ranges:
        if r[0] < min_value:
            min_value = r[0]
    
    end_time = time.perf_counter()


    print(f"{min_value=} in {end_time-start_time}s")
