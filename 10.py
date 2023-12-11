import numpy as np

def parse_file(data_file : str):
    nodes = []
    start = None
    lines = data_file.split('\n')
    for row, line in enumerate(lines):
        node_line = []
        for col, char in enumerate(line):
            if char == '|':
                node_line.append([(row-1, col), (row+1, col)])
            if char == '-':
                node_line.append([(row, col-1), (row, col+1)])
            if char == 'L':
                node_line.append([(row - 1, col), (row, col + 1)])
            if char == 'J': 
                node_line.append([(row - 1, col), (row, col - 1)])
            if char == '7': 
                node_line.append([(row + 1, col), (row, col - 1)])
            if char == 'F': 
                node_line.append([(row + 1, col), (row, col + 1)])
            if char == '.': 
                node_line.append(None)
            if char == 'S':
                node_line.append([])
                start = (row, col)

        nodes.append(node_line)

        #check S
    if start[0] > 0 and lines[start[0] - 1][start[1]] in ['|', '7', 'F']:
        nodes[start[0]][start[1]].append((start[0] - 1, start[1]))

    if start[1] > 0 and lines[start[0]][start[1] - 1] in ['-', 'L', 'F']:
        nodes[start[0]][start[1]].append((start[0], start[1]-1))

    if start[0] < len(nodes) - 1 and lines[start[0] + 1][start[1]] in ['|', 'L', 'J']:
        nodes[start[0]][start[1]].append((start[0]+1, start[1]))

    if start[1] < len(nodes[0]) - 1 and lines[start[0]][start[1] + 1] in ['-', 'J', '7']:
        nodes[start[0]][start[1]].append((start[0], start[1]+1))

    return nodes, start

def Dijksta(nodes, start):
    open_list = [start]
    distances = - np.ones((len(nodes), len(nodes[0])))
    distances[start] = 0

    while len(open_list) > 0:
        open_list.sort(key=lambda node : distances[node])
        current_node = open_list.pop(0)
        for node in nodes[current_node[0]][current_node[1]]:
            if  0 <= node[0] <= len(nodes) - 1 and 0 <= node[1] <= len(nodes[0]) - 1 and distances[node] < 0 : 
                open_list.append(node)
                distances[node] = distances[current_node] + 1

    return distances
        
def count_fill(distances, data):
    lines = data.split('\n')
    filled = np.zeros_like(distances, np.uint8)

    print(distances)

    for row, row_d in enumerate(distances):
        count_edge = 0
        for col, col_d in enumerate(row_d):
            if col_d >= 0 and lines[row][col] in ['|', 'L', 'J']:
                count_edge += 1

            if count_edge % 2 == 1 and col_d < 0:
                filled[row, col] = 255

            previous_distance = col_d

    return filled

if __name__ == "__main__":
    nodes, start = None, None
    with open("./data/10", 'r') as data_file:
        data = data_file.read()
        nodes, start = parse_file(data)

    distances = Dijksta(nodes, start)
    print(distances.max())
    filled = count_fill(distances, data)

    print(np.count_nonzero(filled))