from functools import reduce
from typing import List
import sys

class Day1:
    def solve(self, nums: List[int]) -> int:
        nums = sorted(nums)
        result = self.find3(nums)
        return result[0] * result[1] * result[2]

    def find2(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == 2020:
                    return [nums[i], nums[j]]

    def find3(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if (nums[i] + nums[j] + nums[k]) == 2020:
                        return [nums[i], nums[j], nums[k]]


if __name__ == '__main__':
    path = sys.argv[1]
    file_handle = open(path, 'r')
    line = file_handle.readline()
    list: List[int] = []

    while line:
        list.append(int(line))
        line = file_handle.readline()

    day1 = Day1()
    res = day1.solve(list)

    print(res)
