import numpy as np
def parse_file(data_file : str):
    time_str, dist_str = data_file.split('\n')
    times = list(map(int, time_str.split(": ")[1].strip().split(' ')))
    distances = list(map(int, dist_str.split(": ")[1].strip().split(' ')))

    races = []
    for t, d in zip(times, distances):
        races.append((t, d))
    
    return races

if __name__ == "__main__":
    races = None
    with open("./data/06", 'r') as data_file:
        races = parse_file(data_file.read())

    #part1
    winning_count = 1
    for race in races:
        #Solve the equations, we're not animals...
        # t*(time - t) = distance
        time = race[0]
        distance = race[1] + 1
        delta = time**2 - 4*distance
        min_t = np.ceil((time - np.sqrt(delta))/2)
        max_t = np.floor((time + np.sqrt(delta))/2)
        winning_count *= max_t - min_t + 1

    #part2
    time, distance = None, None
    with open("./data/06", 'r') as data_file:
        time_str, dist_str = data_file.read().split('\n')
        time = float(time_str.split(": ")[1].replace(' ', ''))
        distance = float(dist_str.split(": ")[1].replace(' ', '')) + 1

    delta = time**2 - 4*distance
    min_t = np.ceil((time - np.sqrt(delta))/2)
    max_t = np.floor((time + np.sqrt(delta))/2)
    winning_count = max_t - min_t + 1

    print(winning_count)
