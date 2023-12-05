import re
import numpy as np

def parse_card(string : str):
    left_numbers, right_numbers = string.split(':')[1].split('|')
    left_numbers = list(map(int, re.sub(R'\s+', ' ', left_numbers.strip()).split(" ")))
    right_numbers = list(map(int,  re.sub(R'\s+', ' ',right_numbers.strip()).split(" ")))

    return left_numbers, right_numbers

if __name__ == "__main__":
    data=[]
    with open("./data/04", 'r', encoding="utf-8") as data_file:
        for line in data_file:
            data.append(parse_card(line))

    #part 1
    total_sum : int = 0
    for d in data:
        u = set(d[0]).intersection(set(d[1]))
        if len(u) > 0:
            total_sum += 2**(len(u)-1)

    print(total_sum)

    #part 2
    card_counts = np.ones((len(data),1))

    for i, d in enumerate(data):
        u = set(d[0]).intersection(set(d[1]))
        matches = len(u)
        card_counts[i+1:i+matches+1] += card_counts[i]

    print(np.sum(card_counts))

    

