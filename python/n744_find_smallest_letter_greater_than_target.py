from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        if target < letters[left] or target >= letters[right]:
            return letters[left]
        while left <= right:
            mid = (left + right) // 2
            if target < letters[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return letters[left]

if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "c"
    print(Solution().nextGreatestLetter(letters, target))