class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        target = set(["01", "10"])
        for i in range(0, len(s), 2):
            if s[i:i+2] in target:
                ans += 1
        return ans