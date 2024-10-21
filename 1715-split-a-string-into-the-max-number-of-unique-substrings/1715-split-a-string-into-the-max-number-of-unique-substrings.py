class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        sub = set()
        def backtrack(i, cur_str):
            if i == len(s): return len(sub)
            cur_str += s[i]
            ans = backtrack(i+1, cur_str)
            if cur_str not in sub:
                sub.add(cur_str)
                ans = max(ans, backtrack(i+1, ""))
                sub.remove(cur_str)
            return ans
            
        return backtrack(0, "")