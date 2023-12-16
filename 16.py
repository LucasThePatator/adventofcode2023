import numpy as np
def propagate(data, position, direction, energy_grid):
    if position[0] < 0 or position[1] < 0 or position[0] >= data.shape[0] or position[1] >= data.shape[1]:
        return

    char = data[position]
    energy_grid[position] = max(1, energy_grid[position])

    if direction == 'R':
        while char == '.' or char == '-':
            position = (position[0], position[1] + 1)
            if position[1] >= data.shape[1]:
                return

            char = data[position]
            energy_grid[position] = max(1, energy_grid[position])

        if char == '/':
            propagate(data, (position[0] - 1, position[1]), 'U', energy_grid)

        if char == '\\':
            propagate(data, (position[0] + 1, position[1]), 'D', energy_grid)

        if char == '|':
            if energy_grid[position] != 2: #Beam has split here
                energy_grid[position] = 2
                propagate(data, (position[0] - 1, position[1]), 'U', energy_grid)
                propagate(data, (position[0] + 1, position[1]), 'D', energy_grid)

    if direction == 'L':
        while char == '.' or char == '-':
            position = (position[0], position[1] - 1)
            if position[1] < 0:
                return

            char = data[position]
            energy_grid[position] = max(1, energy_grid[position])

        if char == '/':
            propagate(data, (position[0] + 1, position[1]), 'D', energy_grid)

        if char == '\\':
            propagate(data, (position[0] - 1, position[1]), 'U', energy_grid)

        if char == '|':
            if energy_grid[position] != 2: #Beam has split here
                energy_grid[position] = 2
                propagate(data, (position[0] - 1, position[1]), 'U', energy_grid)
                propagate(data, (position[0] + 1, position[1]), 'D', energy_grid)

    if direction == 'D':
        while char == '.' or char == '|':
            position = (position[0] + 1, position[1])
            if position[0] >= len(data):
                return

            char = data[position]
            energy_grid[position] = max(1, energy_grid[position])

        if char == '/':
            propagate(data, (position[0], position[1] - 1), 'L', energy_grid)

        if char == '\\':
            propagate(data, (position[0], position[1] + 1), 'R', energy_grid)

        if char == '-':
            if energy_grid[position] != 2: #Beam has split here
                energy_grid[position] = 2
                propagate(data, (position[0], position[1] - 1), 'L', energy_grid)
                propagate(data, (position[0], position[1] + 1), 'R', energy_grid)

    if direction == 'U':
        while char == '.' or char == '|':
            position = (position[0] - 1, position[1])
            if position[0] < 0:
                return

            char = data[position]
            energy_grid[position] = max(1, energy_grid[position])

        if char == '/':
            propagate(data, (position[0], position[1] + 1), 'R', energy_grid)

        if char == '\\':
            propagate(data, (position[0], position[1] - 1), 'L', energy_grid)

        if char == '-':
            if energy_grid[position] != 2: #Beam has split here
                energy_grid[position] = 2
                propagate(data, (position[0], position[1] - 1), 'L', energy_grid)
                propagate(data, (position[0], position[1] + 1), 'R', energy_grid)

def main():
    with open("./data/16", 'r') as data_file:
        data = data_file.read().split('\n')

    grid = np.empty((len(data), len(data[0])), dtype=str)
    for row, line in enumerate(data):
        grid[row, :] = [*line]

    energy_grid = np.zeros_like(grid, dtype=np.uint8)
    propagate(grid, (0,0), 'R', energy_grid)
    print(np.count_nonzero(energy_grid))

    max_value = 0
    #vertical
    for row in range(grid.shape[0]):
        energy_grid = np.zeros_like(grid, dtype=np.uint8)
        propagate(grid, (row, 0), 'R', energy_grid)
        max_value = max(max_value, np.count_nonzero(energy_grid))

        energy_grid = np.zeros_like(grid, dtype=np.uint8)
        propagate(grid, (row, grid.shape[1] - 1), 'L', energy_grid)
        max_value = max(max_value, np.count_nonzero(energy_grid))

    #horizontal
    for col in range(grid.shape[1]):
        energy_grid = np.zeros_like(grid, dtype=np.uint8)
        propagate(grid, (0, col), 'D', energy_grid)
        max_value = max(max_value, np.count_nonzero(energy_grid))

        energy_grid = np.zeros_like(grid, dtype=np.uint8)
        propagate(grid, (grid.shape[0] - 1, col), 'U', energy_grid)
        max_value = max(max_value, np.count_nonzero(energy_grid))

    print(max_value)

if __name__ == "__main__":
    main()