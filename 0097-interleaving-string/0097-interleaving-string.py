class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = [ [[-1]*(len(s3)+1) for _ in range(len(s2)+1)] for _ in range(len(s1)+1) ]
        def dp(i, j, k):
            if k == len(s3):
                if i == len(s1) and j == len(s2): return 1
                return 0
            if i == len(s1) and j == len(s2): return 0
            if cache[i][j][k] != -1: return cache[i][j][k]
            cache[i][j][k] = 0
            if i < len(s1) and s3[k] == s1[i]:
                cache[i][j][k] |= dp(i+1, j, k+1)
            if j < len(s2) and s3[k] == s2[j]:
                cache[i][j][k] |= dp(i, j+1, k+1)
            return cache[i][j][k]
        
        return dp(0, 0, 0) == 1