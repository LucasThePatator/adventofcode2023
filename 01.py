
def first_part():
    with open('./data/01') as data:
        sum : int = 0
        for line in data:
            #get first one
            number : str = ''
            for c in line:
                if ord('0') <= ord(c) <= ord('9'):
                    number += c
                    break
            
            #get second one
            for c in reversed(line):
                if ord('0') <= ord(c) <= ord('9'):
                    number += c
                    break

            sum += int(number)
        print(sum)


def second_part():
    with open('./data/01') as data:
        sum : int = 0
        for line in data:
            number = ''
            values = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

            index = 2**32
            temp_val = None
            #first_one
            for i, c in enumerate(line):
                if ord('0') <= ord(c) <= ord('9'):
                    index = i
                    temp_val = c
                    break

            for i, v in enumerate(values):
                pos = line.find(v)
                if pos >= 0 and pos < index:
                    index = pos
                    temp_val = str(i)
                    
            number += temp_val

            temp_val = None
            index = 2**32
            #second_one
            for i, c in enumerate(reversed(line)):
                if ord('0') <= ord(c) <= ord('9'):
                    index = i
                    temp_val = c
                    break

            for i, v in enumerate(values):
                pos = line[::-1].find(v[::-1])
                if pos >= 0 and pos < index:
                    index = pos
                    temp_val = str(i)
                    

            number += temp_val
            print(number)
            sum += int(number)
        print(sum)

if __name__ == "__main__":
    second_part()
