from typing import List, Dict, Tuple

def is_symbol(char : str) -> bool:
    return char != '.' and not char.isdigit()

def check_star(row : int, col : int, grid : List[List[str]], stars_list : List[Tuple[int, int]]):
    if grid[row][col] == '*':
        stars_list.append((row, col))

def find_valid_numbers(grid : str) -> (List[int], Dict):
    ret = []
    stars_numbers = {}

    for row, line in enumerate(grid):
        in_number : bool = False
        current_number = ''
        current_number_is_valid = False
        touch_stars = []
        for col, c in enumerate(line):
            if c.isdigit():
                current_number+=c
                if not current_number_is_valid:
                    if not in_number and col > 0: #new number, check to the left
                        if row > 0:
                            current_number_is_valid = current_number_is_valid or is_symbol(grid[row-1][col-1])
                            check_star(row-1, col-1, grid, touch_stars)
                            
                        current_number_is_valid = current_number_is_valid or is_symbol(grid[row][col-1])
                        check_star(row, col-1, grid, touch_stars)

                        if row < len(grid) - 1:
                            current_number_is_valid = current_number_is_valid or is_symbol(grid[row + 1][col-1])
                            check_star(row + 1, col - 1, grid, touch_stars)


                    #Check if top or bottom are valid
                    if row > 0:
                        current_number_is_valid = current_number_is_valid or is_symbol(grid[row-1][col])
                        check_star(row - 1, col, grid, touch_stars)


                    if row < len(grid) - 1:
                        current_number_is_valid = current_number_is_valid or is_symbol(grid[row + 1][col])
                        check_star(row + 1, col, grid, touch_stars)

                in_number = True

            elif in_number:
                if not current_number_is_valid: #check to the right
                    if row > 0:
                        current_number_is_valid = current_number_is_valid or is_symbol(grid[row - 1][col])
                        check_star(row - 1, col, grid, touch_stars)

                    current_number_is_valid = current_number_is_valid or is_symbol(grid[row][col])
                    check_star(row, col, grid, touch_stars)

                    if row < len(grid) - 1:
                        current_number_is_valid = current_number_is_valid or is_symbol(grid[row + 1][col])
                        check_star(row + 1, col, grid, touch_stars)


                current_number = int(current_number)
                if current_number_is_valid:
                    ret.append(current_number)
                    for star in touch_stars:
                        if star not in stars_numbers:
                            stars_numbers[star] = [current_number]
                        else:
                            stars_numbers[star].append(current_number)

                touch_stars = []
                current_number_is_valid = False
                current_number = ''
                in_number = False

        if in_number:
            current_number = int(current_number)
            if current_number_is_valid:
                ret.append(current_number)
                for star in touch_stars:
                    if star not in stars_numbers:
                        stars_numbers[star] = [current_number]
                    else:
                        stars_numbers[star].append(current_number)

        touch_stars = []
        current_number_is_valid = False
        current_number = ''
        in_number = False


    return ret, stars_numbers


if __name__ == "__main__":
    data : str = None
    with open('./data/03', 'r', encoding='utf-8') as data_file:
        data = data_file.read()

    valid_numbers, stars_numbers = find_valid_numbers(data.split('\n'))
    total_sum = sum(valid_numbers)
    print(total_sum)

    total_sum = 0
    for key in stars_numbers.keys():
        if len(stars_numbers[key]) != 2:
            continue

        total_sum += stars_numbers[key][0] * stars_numbers[key][1]

    print(total_sum)
