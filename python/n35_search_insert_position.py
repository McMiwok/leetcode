from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return left

if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 2
    print(Solution().searchInsert(nums, target))