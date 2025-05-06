class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2
            res = self.guess(mid)
            if res == -1:
                right = mid - 1
            elif res == 1:
                left = mid + 1
            else:
                return mid

    def guess(self, num: int) -> int:
        picked_number = pick
        if num > picked_number:
            return -1
        elif num < picked_number:
            return 1
        else:
            return 0

if __name__ == "__main__":
    n = 10
    pick = 6
    print(Solution().guessNumber(10))