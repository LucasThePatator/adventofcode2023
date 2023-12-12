import numpy as np

def parse_file(data : str):
    lines = data.split('\n')
    universe = np.zeros((len(lines), len(lines[0])))
    for row, line in enumerate(lines):
        universe[row, :] =  np.array(list(map(lambda c : 0 if c == '.' else '1', line)))

    return universe, np.argwhere(universe > 0)

def find_empty(universe):
    col_sum = np.sum(universe, axis = 0)
    cols = np.argwhere(col_sum == 0)
    row_sum = np.sum(universe, axis = 1)
    rows = np.argwhere(row_sum == 0)

    return rows, cols

def find_paths_distances(stars, empty_rows, empty_cols, factor):
    distance = 0
    for i, s1 in enumerate(stars[:-1, :]):
        for s2 in stars[i+1:, :]:
            row_start = min(s1[0], s2[0])
            row_end = max(s1[0], s2[0]) 
            distance += row_end - row_start
            for empty_row in empty_rows:
                if row_start < empty_row < row_end:
                    distance += factor - 1

            col_start = min(s1[1], s2[1])
            col_end = max(s1[1], s2[1]) 
            distance += col_end - col_start
            for empty_col in empty_cols:
                if col_start < empty_col < col_end:
                    distance += factor - 1

    return distance

if __name__ == "__main__":
    with open("./data/11", 'r') as data_file:
        universe, stars = parse_file(data_file.read())
    
    print(stars)
    empty_rows, empty_cols = find_empty(universe)
    distance = find_paths_distances(stars, empty_rows, empty_cols, 2)
    print(distance)
    distance = find_paths_distances(stars, empty_rows, empty_cols, 1_000_000)
    print(distance)