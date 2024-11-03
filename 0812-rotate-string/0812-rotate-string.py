class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        for i in range(len(s)):
            ss = s[i:] + s[:i]
            if ss == goal: return True
        return False