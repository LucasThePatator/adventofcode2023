from collections import OrderedDict

def get_hash(string : str):
    value = 0
    for c in string:
        value += ord(c)
        value *= 17
        value %= 256

    return value

def main():
    with open("./data/15", 'r') as data_file:
        strings = data_file.read().split(',')

    total_value = 0
    for string in strings:
        value = get_hash(string)
        total_value += value

    print(total_value)

    boxes = {}
    for i in range(256):
        boxes[i] = OrderedDict()

    for string in strings:
        if '=' in string:
            label = string[0:-2]
            lens = int(string[-1:])
            box = get_hash(label)
            boxes[box][label] = int(lens)
        else:
            label = string[0:-1]
            box = get_hash(label)
            if label in boxes[box].keys():
                boxes[box].pop(label)

    total_value = 0
    for box in boxes.keys():
        lenses = boxes[box]
        for pos, label in enumerate(lenses.keys()):
            total_value += (box + 1) * (pos + 1) * lenses[label]

    print(total_value)
    
if __name__ == "__main__":
    main()