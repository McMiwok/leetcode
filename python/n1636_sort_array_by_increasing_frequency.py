from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        nums.sort(key=lambda n: (frequency[n], -n))

        return nums

if __name__ == "__main__":
    nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    print(Solution().frequencySort(nums))