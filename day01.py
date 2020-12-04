from functools import reduce
from typing import List, Tuple
import sys


# map the indexes with True or False which means if that index can be used to add up to 2020
# this algorithm uses backtracking with depth-first technique to find the sum
def map_indexes(values: List[int], idx: int, node: Tuple[int, int], acc: List[bool]) -> Tuple[List[bool], bool]:
    if node[0] > 2020 or node[1] <= 0:
        return acc, False
    elif node[0] == 2020 and len(list(filter(lambda x: x, acc))) == 3:
        return acc, True
    else:
        left = map_indexes(values, idx + 1, (node[0] + values[idx], node[1] - values[idx]), acc + [True])
        if left[1]:
            return left[0], True
        else:
            right = map_indexes(values, idx + 1, (node[0], node[1] - values[idx]), acc + [False])
            if right[1]:
                return right[0], True
            else:
                acc.pop()
                return acc, False


if __name__ == '__main__':
    path = sys.argv[1]
    file_handle = open(path, 'r')
    line = file_handle.readline()
    nums: List[int] = []

    while line:
        nums.append(int(line))
        line = file_handle.readline()

    total = reduce(lambda a, b: a + b, nums)
    index_map = map_indexes(nums, 0, (0, total), [])
    result = []

    for i in range(0, len(nums)):
        if i < len(index_map[0]) and index_map[0][i]:
            result.append(nums[i])

    print(reduce(lambda a, b: a * b, result))
