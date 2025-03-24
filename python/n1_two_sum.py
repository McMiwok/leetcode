from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        known_numbers = {}
        for i, num in enumerate(nums):
            desire = target - num
            if desire in known_numbers:
                return [known_numbers[desire], i]
            known_numbers[num] = i

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums, target))