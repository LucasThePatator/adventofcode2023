
card_values = "AKQJT98765432"
card_values2 = "AKQT98765432J"

from operator import itemgetter

def get_hand_type(hand : str):
    counts = [0 for _ in card_values]
    for i, v in enumerate(card_values):
        counts[i] = hand.count(v)

    counts.sort(reverse=True)

    set_type = 0
    if counts[0] == 5:
        set_type = 7
    elif counts[0] == 4:
        set_type = 6
    elif counts[0] == 3 and counts[1] == 2:
        set_type = 5
    elif counts[0] == 3:
        set_type = 4
    elif counts[0] == 2 and counts[1] == 2:
        set_type = 3
    elif counts[0] == 2:
        set_type = 2
    else:
        set_type = 1
    
    return set_type

def evaluate_hand1(hand : str):
    set_type = get_hand_type(hand)
    hand_value =  set_type * 20**5
    for i, c in enumerate(hand):
        hand_value += (14 - card_values.index(c)) * 20**(4-i)
    return hand_value

def evaluate_hand2(hand : str):

    set_type = 0
    for c in card_values:
        new_hand = hand.replace('J', c)
        local_set_type = get_hand_type(new_hand)
        set_type = max(set_type, local_set_type)

    hand_value =  set_type * 20**5
    for i, c in enumerate(hand):
        hand_value += (14 - card_values2.index(c)) * 20**(4-i)
    return hand_value

def parse_file(data_file : str):
    hands = []
    
    for line in data_file.split('\n'):
        hand, value = line.split(" ")
        hands.append([hand.strip(), int(value)])

    return hands

if __name__ == "__main__":
    hands = None
    with open("./data/07", 'r') as data_file:
        hands = parse_file(data_file.read())

    hand_values = []
    for hand in hands:
        if False:
            hand_value = evaluate_hand1(hand[0])
        else :
            hand_value = evaluate_hand2(hand[0])
        hand.append(hand_value)

    hands.sort(key=itemgetter(2))
    print(hands)
    score = 0
    for i, h in enumerate(hands):
        score += (i+1) * h[1]

    print(score)