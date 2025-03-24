from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        if not heights:
            return 0

        excepted = sorted(heights)
        count = 0

        for i in range(len(heights)):
            if excepted[i] != heights[i]:
                count += 1

        return count

if __name__ == "__main__":
    heights = [1, 1, 4, 2, 1, 3]
    print(Solution().heightChecker(heights))