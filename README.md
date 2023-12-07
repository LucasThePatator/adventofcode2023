# adventofcode2023
This will be full of spoilers, be warned

## Day 1
For star 1, I just search both ways for the first number in each line of the data, pretty simple.
To capitalize on star 1 I treat the spelled numbers in a separate case. It felt simpler to search the reversed numbers in the reversed string. Cute trick I guess

## Day 2
I mean, there's not much to say, it's just counting. Parsing was the most "difficult" part.

## Day3
OK this was a bit long to do. I opted to parse the entire data character by character while maintaining a state of whether I'm currently parsing a number or not. That way I can start checking for symbols at the same time around the current character. Boundary checking was a bitch..
For star 2, I had to also maintain a state of all the stars encountered during the parsing of the number. A map of stars to list of numbers is populated when finishing parsing a number.
