from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]

if __name__ == "__main__":
    numbers = [2, 3, 4]
    target = 6
    print(Solution().twoSum(numbers, target))