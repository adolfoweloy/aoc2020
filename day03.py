import sys
from functools import reduce
from typing import List

RIGHT = 1
DOWN = -1


def multiply(a: int, b: int) -> int:
    return a * b


if __name__ == '__main__':
    path = sys.argv[1]
    file_handle = open(path, 'r')

    # building the map
    my_map = []
    line = file_handle.readline().rstrip()
    while line:
        my_map.append(line)
        line = file_handle.readline().rstrip()

    # preps
    counts: List[int] = []
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for slope in slopes:
        i: int = 0
        direction = RIGHT
        trees: int = 0
        line: str = my_map[0]
        map_size = len(my_map)
        width: int = len(line)
        position = 0

        while True:
            coordinate = 0 if direction == RIGHT else 1
            if direction == RIGHT:
                position = (position + slope[coordinate]) % width

            if direction == DOWN:
                i = i + slope[coordinate]
                if i >= map_size:
                    break
                line = my_map[i]
                if line[position] == "#":
                    trees = trees + 1

            direction = direction * -1
        counts.append(trees)

    print(reduce(multiply, counts))
