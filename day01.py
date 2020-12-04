import sys
from functools import reduce
from typing import List


# the solution for this problem solves both part 1 and part 2
# the parameter size is what makes the difference here for part1 and part 2
def find_numbers(candidates: List[int], combination: List[int], total_sum: int, start: int, target: int, acc: List[int],
                 size: int):
    for i in range(start, len(candidates)):
        # boundary for this depth-first search
        if total_sum > target or len(acc) > 0:
            break

        # backtracking
        combination.append(candidates[i])
        find_numbers(candidates, combination, total_sum + candidates[i], i + 1, target, acc, size)
        combination.pop()

        # saving the result when sum == target (I don't like this solution)
        if total_sum == target and size == len(combination):
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

    find_numbers(nums, [], 0, 0, 2020, result, 2)

    print(reduce(lambda a, b: a * b, result))
