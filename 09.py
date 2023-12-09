import numpy as np

def parse_file(data_file : str):
    rows = data_file.split('\n')
    sequences = []
    for row in rows:
        sequence = list(map(int, row.split(' ')))
        sequences.append(np.array(sequence))

    return sequences

def get_next_number(sequence : np.ndarray):
    current_sequence = sequence
    count = 0
    last_values = [current_sequence[-1]]
    while not ((current_sequence - current_sequence[0]) == 0).all():
        current_sequence = current_sequence[1:] - current_sequence[:-1]
        last_values.append(current_sequence[-1])
        count += 1

    new_val = 0
    for i in range(count + 1):
        new_val += last_values.pop()

    return new_val

if __name__ == "__main__":

    sequences = None
    with open("./data/09", 'r') as data_file:
        sequences = parse_file(data_file.read())

    total_sum = 0
    for s in sequences:
        total_sum += get_next_number(s)

    print(total_sum)

    total_sum = 0
    for s in sequences:
        total_sum += get_next_number(s[::-1])

    print(total_sum)