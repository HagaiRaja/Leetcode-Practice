class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        last0 = 0
        for i in range(len(s)):
            if s[i] == "0":
                ans += i-last0
                last0 += 1
        return ans