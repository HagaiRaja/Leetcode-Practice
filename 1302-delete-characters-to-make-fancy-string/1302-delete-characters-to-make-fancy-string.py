class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = "00"
        for c in s:
            if c != ans[-1] or c != ans[-2]:
                ans += c
        return ans[2:]