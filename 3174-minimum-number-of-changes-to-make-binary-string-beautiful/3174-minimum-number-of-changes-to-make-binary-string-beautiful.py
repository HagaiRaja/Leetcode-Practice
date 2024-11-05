class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        for i in range(0, len(s), 2):
            if s[i:i+2] in ["01", "10"]:
                ans += 1
        return ans