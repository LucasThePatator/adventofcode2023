import numpy as np

def parse_file(data_file):
    lines = data_file.read().split('\n')
    
    grid = np.empty((len(lines), len(lines[0])))
    for row, line in enumerate(lines):
        grid[row, :] = np.array(list(map(int, line)))

    return grid

def update_distance(distances, previous, node, current_node, grid, ):
    new_distance =  distances[current_node] + grid[node[0], node[1]]
    if distances[node] > 0:
        if new_distance < distances[node]:
            distances[node] = new_distance
            previous[node] = current_node
    else :
        distances[node] = new_distance
        previous[node] = current_node


def check_path(grid, node, previous):
    path = grid.copy()
    current_node = node
    while current_node in previous.keys():
        path[current_node[0], current_node[1]] = '-1'
        current_node = previous[current_node]

    print(path)

def a_star(grid, position):
    distances = np.zeros((*grid.shape, 10 + 1, 4), dtype=np.float32)
    previous = dict()
    open_set = set()
    current_node = ((*position, 0, ' '))
    visited_set = np.zeros((*grid.shape, 10 + 1, 4), dtype=np.uint8)

    v = {'L' : 0, 'R' : 1, 'U' : 2, 'D' : 3}

    open_set.add((position[0] + 1, position[1], 1, v['D']))
    open_set.add((position[0], position[1] + 1, 1, v['R']))

    distances[(position[0] + 1, position[1], 1, v['D'])] = grid[(position[0] + 1, position[1])]
    distances[(position[0], position[1] + 1, 1, v['R'])] = grid[(position[0], position[1] + 1)]
    previous[(position[0] + 1, position[1], 1, v['D'])] = current_node
    previous[(position[0], position[1] + 1, 1, v['R'])] = current_node

    end_distances = []

    while len(open_set) > 0:
        current_node = min(open_set, key = lambda node : distances[node])# + grid.shape[0] - node[0] + grid.shape[1] - node[1])
        open_set.remove(current_node)
        visited_set[current_node] = 1

        if current_node[0] == grid.shape[0] - 1 and current_node[1] ==  grid.shape[1] - 1:
            end_distances.append(distances[current_node])
            check_path(grid, current_node, previous)
            pass

        if current_node[3] != v['L'] and current_node[1] < grid.shape[1] - 1 and not (current_node[3] == v['R'] and current_node[2] == 3) :
            count = current_node[2] + 1 if current_node[3] == v['R'] else 1
            new_node = (current_node[0], current_node[1] + 1, count, v['R'])

            if visited_set[new_node] == 0:
                open_set.add(new_node)
                update_distance(distances, previous, new_node, current_node, grid)
                
        if current_node[3] != v['R'] and current_node[1] > 0 and not (current_node[3] == v['L'] and current_node[2] == 3) :
            count = current_node[2] + 1 if current_node[3] == v['L'] else 1
            new_node = (current_node[0], current_node[1] - 1, count, v['L'])

            if visited_set[new_node] == 0:
                open_set.add(new_node)
                update_distance(distances, previous, new_node, current_node, grid)

        if current_node[3] != v['U'] and current_node[0] < grid.shape[0] - 1 and not (current_node[3] == v['D'] and current_node[2] == 3) :
            count = current_node[2] + 1 if current_node[3] == v['D'] else 1
            new_node = (current_node[0] + 1, current_node[1], count, v['D'])

            if visited_set[new_node] == 0:
                open_set.add(new_node)
                update_distance(distances, previous, new_node, current_node, grid)


        if current_node[3] != v['D'] and current_node[0] > 0 and not (current_node[3] == v['U'] and current_node[2] == 3):
            count = current_node[2] + 1 if current_node[3] == v['U'] else 1
            new_node = (current_node[0] - 1, current_node[1], count, v['U'])
            
            if visited_set[new_node] == 0:
                open_set.add(new_node)
                update_distance(distances, previous, new_node, current_node, grid)
    
    print(min(end_distances))

def a_star2(grid, position):
    distances = np.zeros((*grid.shape, 10 + 1, 4), dtype=np.float32)
    previous = dict()
    open_set = set()
    current_node = ((*position, 0, ' '))
    visited_set = np.zeros((*grid.shape, 10 + 1, 4), dtype=np.bool_)

    v = {'L' : 0, 'R' : 1, 'U' : 2, 'D' : 3}

    open_set.add((position[0] + 1, position[1], 1, v['D']))
    open_set.add((position[0], position[1] + 1, 1, v['R']))

    distances[(position[0] + 1, position[1], 1, v['D'])] = grid[(position[0] + 1, position[1])]
    distances[(position[0], position[1] + 1, 1, v['R'])] = grid[(position[0], position[1] + 1)]

    end_distances = []

    while len(open_set) > 0:
        current_node = min(open_set, key = lambda node : distances[node])# + grid.shape[0] - node[0] + grid.shape[1] - node[1])
        open_set.remove(current_node)
        visited_set[current_node] = 1

        if current_node[0] == grid.shape[0] - 1 and current_node[1] ==  grid.shape[1] - 1:
            end_distances.append(distances[current_node])
            #check_path(grid, current_node, previous)
            pass

        if current_node[3] != v['L'] and current_node[1] < grid.shape[1] - 1 and not (current_node[3] == v['R'] and current_node[2] == 10) and not ( current_node[3] in [v['U'], v['D']] and (current_node[2] < 4 or current_node[1] >= grid.shape[1] - 4)):
            count = current_node[2] + 1 if current_node[3] == v['R'] else 1
            new_node = (current_node[0], current_node[1] + 1, count, v['R'])

            if visited_set[new_node] == 0:
                open_set.add(new_node)
                update_distance(distances, previous, new_node, current_node, grid)
                
        if current_node[3] != v['R'] and current_node[1] > 0 and not (current_node[3] == v['L'] and current_node[2] == 10)  and not ( current_node[3] in [v['U'], v['D']] and (current_node[2] < 4 or current_node[1] <= 3)):
            count = current_node[2] + 1 if current_node[3] == v['L'] else 1
            new_node = (current_node[0], current_node[1] - 1, count, v['L'])

            if visited_set[new_node] == 0:
                open_set.add(new_node)
                update_distance(distances, previous, new_node, current_node, grid)

        if current_node[3] != v['U'] and current_node[0] < grid.shape[0] - 1 and not (current_node[3] == v['D'] and current_node[2] == 10)  and not ( current_node[3] in [v['R'], v['L']] and (current_node[2] < 4 or current_node[0] >= grid.shape[0] - 4)):
            count = current_node[2] + 1 if current_node[3] == v['D'] else 1
            new_node = (current_node[0] + 1, current_node[1], count, v['D'])

            if visited_set[new_node] == 0:
                open_set.add(new_node)
                update_distance(distances, previous, new_node, current_node, grid)


        if current_node[3] != v['D'] and current_node[0] > 0 and not (current_node[3] == v['U'] and current_node[2] == 10)  and not ( current_node[3] in [v['R'], v['L']] and (current_node[2] < 4 or current_node[0] <= 3)):
            count = current_node[2] + 1 if current_node[3] == v['U'] else 1
            new_node = (current_node[0] - 1, current_node[1], count, v['U'])

            if visited_set[new_node] == 0:
                open_set.add(new_node)
                update_distance(distances, previous, new_node, current_node, grid)
    
    print(min(end_distances))

def main():
    with open("./data/17", 'r') as data_file:
        grid = parse_file(data_file)

    a_star2(grid, (0,0))

if __name__ == "__main__":
    main()



