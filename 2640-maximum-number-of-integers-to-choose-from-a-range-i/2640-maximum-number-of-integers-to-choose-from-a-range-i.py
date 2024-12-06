class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        total, ins = 0, 0
        for i in range(1, n+1):
            if i in banned: continue
            if total + i <= maxSum:
                total += i
                ins += 1
            else:
                break
        return ins
