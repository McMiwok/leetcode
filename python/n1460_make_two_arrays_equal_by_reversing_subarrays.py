from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False

        target_counts = {}
        for num in target:
            target_counts[num] = target_counts.get(num, 0) + 1

        arr_counts = {}
        for num in arr:
            arr_counts[num] = arr_counts.get(num, 0) + 1

        return target_counts == arr_counts

if __name__ == "__main__":
    target, arr = [1,2,3,4], [2,4,1,3]
    print(Solution().canBeEqual(target, arr))