from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ptr1 = 0
        ptr2 = 0
        result = []

        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] == nums2[ptr2]:
                if not result or nums1[ptr1] != result[-1]:
                    result.append(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
            elif nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1

        return result

if __name__ == "__main__":
    nums1, nums2 = [1,2,2,1], [2,2]
    print(Solution().intersection(nums1, nums2))