from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            left_sorted = merge_sort(left_half)
            right_sorted = merge_sort(right_half)

            return merge(left_sorted, right_sorted)

        def merge(left, right):
            merged = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            while i < len(left):
                merged.append(left[i])
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1
            return merged

        return merge_sort(nums)

if __name__ == "__main__":
    nums = [5,1,1,2,0,0]
    print(Solution().sortArray(nums))