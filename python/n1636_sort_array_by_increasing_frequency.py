from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        sorted_nums = sorted(nums, key=lambda x: (frequency[x], -x))

        return sorted_nums

if __name__ == "__main__":
    nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    print(Solution().frequencySort(nums))