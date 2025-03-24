from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_counts = {}
        for num in nums:
            color_counts[num] = color_counts.get(num, 0) + 1

        index = 0
        for color in range(3):
            count = color_counts.get(color, 0)
            for _ in range(count):
                nums[index] = color
                index += 1