from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        counts = {}
        for i in arr1:
            counts[i] = counts.get(i, 0) + 1

        for v in arr2:
            if v in counts:
                result.extend([v] * counts[v])
                del counts[v]

        remaining = sorted(counts.keys())
        for v in remaining:
            result.extend([v] * counts[v])

        return result

if __name__ == "__main__":
    arr1, arr2 = [2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]
    print(Solution().relativeSortArray(arr1,arr2))