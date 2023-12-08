from dataclasses import dataclass
from typing import Dict, List
from copy import copy
from math import lcm

def find_node(nodes : Dict, start : str, end : str, sequence : List[int]):
    current_node = start
    steps = 0
    seq_length = len(sequence)
    seq_index = 0
    while current_node != end:
        current_node = nodes[current_node][sequence[seq_index]]
        seq_index += 1
        seq_index %= seq_length
        steps += 1

    return steps

def find_node_z(nodes : Dict, start : str, sequence : List[int]):
    current_node = start
    steps = 0
    seq_length = len(sequence)
    seq_index = 0
    while current_node[2] != "Z":
        current_node = nodes[current_node][sequence[seq_index]]
        seq_index += 1
        seq_index %= seq_length
        steps += 1

    return steps

def parse_file(data_file : str):
    blocks = data_file.split("\n")
    sequence = list(map(lambda c : 0 if c=='L' else 1, blocks[0]))
    nodes = {}
    for block in blocks[2:]:
        name, children = block.replace(' ', '').split("=")
        nodes[name]=children[1:-1].split(',')

    return nodes, sequence

def check_nodes_z(nodes : List[str]):
    for n in nodes:
        if n[2] != "Z":
            return False
    
    return True

def find_start_nodes(nodes : Dict):
    start_nodes = []
    for n in nodes.keys():
        if n[2] == "A":
            start_nodes.append(n)
    
    return start_nodes


if __name__ == "__main__":
    nodes, sequence = None, None
    with open("./data/08", 'r') as data_file:
        nodes, sequence = parse_file(data_file.read())

    #steps = find_node(nodes, "AAA", "ZZZ", sequence)
    #print(steps)
    start_nodes = find_start_nodes(nodes)
    lcm_all = 1
    for s in start_nodes:
        lcm_all = lcm(find_node_z(nodes, s, sequence), lcm_all)
    print(lcm_all)
