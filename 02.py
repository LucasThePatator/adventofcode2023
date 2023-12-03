import functools

def parse_game(game_line : str):
    id_line, draw_line = game_line.split(":")
    game_id = int(id_line.split(" ")[1])
    draws = []
    draws_lines = draw_line.split(";")

    for d in draws_lines:
        new_draw = [0, 0, 0] #R, G, B
        color_counts = d.split(',')
        for c in color_counts:
            c_stripped = c.lstrip().rstrip()
            count, color = c_stripped.split(" ")

            if color == 'red':
                new_draw[0] = int(count)
            if color == 'green':
                new_draw[1] = int(count)
            if color == 'blue':
                new_draw[2] = int(count)

        draws.append(new_draw)

    return game_id, draws

def first_part():
    games = []

    with open('./data/02', 'r', encoding="utf-8") as data_file:
        for line in data_file:
            game_id, draws = parse_game(line)
            games.append([game_id, draws])

    total_sum = 0
    for game in games:
        is_good = True
        for draw in game[1]:
            if draw[0] > 12 or draw[1] > 13 or draw[2] > 14:
                is_good = False
                break
        
        if is_good:
            total_sum += game[0]

    print(total_sum)

def second_part():
    games = []
    with open('./data/02', 'r', encoding="utf-8") as data_file:
        for line in data_file:
            game_id, draws = parse_game(line)
            games.append([game_id, draws])

    total_sum = 0

    for game in games:
        min_set = game[1][0]
        for draw in game[1][1:]:
            min_set = [max(min_set[0], draw[0]), max(min_set[1], draw[1]), max(min_set[2], draw[2])]
 
        power = functools.reduce(lambda a, b : a*b, min_set)
        total_sum += power

    print(total_sum)

if __name__ == "__main__":
    first_part()
    second_part()
