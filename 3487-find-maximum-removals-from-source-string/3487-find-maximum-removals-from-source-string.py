class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        t = set(targetIndices)

        cache = [[-9999999]*(len(pattern)+1) for _ in range(len(source)+1)]
        def dp(si, pi):
            if cache[si][pi] != -9999999: return cache[si][pi]
            if si == len(source):
                if pi == len(pattern): return 0
                else: return -1e6

            ans = int(si in t) + dp(si+1, pi)
            if pi < len(pattern) and source[si] == pattern[pi]:
                ans = max(ans, dp(si+1, pi+1))
            cache[si][pi] = ans
            return ans

        return dp(0,0)