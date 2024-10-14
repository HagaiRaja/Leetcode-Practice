class Solution:
    def trailingZeroes(self, n: int) -> int:
        # finding all 5s
        ans = 0
        cur = 5
        while cur <= n:
            ans += (n//cur)
            cur *= 5
        return ans