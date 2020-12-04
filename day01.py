import sys
from functools import reduce
from typing import List


def find_numbers(candidates: List[int], combination: List[int], sum: int, start: int, target: int, acc: List[int]):
    for i in range(start, len(candidates)):
        # boundary for this depth-first search
        if sum > target or len(acc) > 0:
            break

        # backtracking
        combination.append(candidates[i])
        find_numbers(candidates, combination, sum + candidates[i], i + 1, target, acc)
        combination.pop()

        # saving the result when sum == target (I don't like this solution)
        if sum == target:
            for c in combination:
                acc.append(c)
            return


if __name__ == '__main__':
    path = sys.argv[1]
    nums: List[int] = []
    result: List[int] = []

    # collecting the lines
    with open(path, 'r') as reader:
        for line in reader.readlines():
            nums.append(int(line))

    find_numbers(nums, [], 0, 0, 2020, result)

    print(reduce(lambda a,b: a * b, result))
