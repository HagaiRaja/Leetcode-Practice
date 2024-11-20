class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        ch2idx = {"a": 0, "b": 1, "c": 2}
        left = [[0]*3 for _ in range(len(s)+1)]
        for i in range(len(s)):
            left[i+1][0] = left[i][0]
            left[i+1][1] = left[i][1]
            left[i+1][2] = left[i][2]
            left[i+1][ch2idx[s[i]]] += 1
        right = [[0]*3 for _ in range(len(s)+1)]
        for i in range(len(s)-1, -1, -1):
            right[i][0] = right[i+1][0]
            right[i][1] = right[i+1][1]
            right[i][2] = right[i+1][2]
            right[i][ch2idx[s[i]]] += 1

        def check(l):
            for i in range(l+1):
                good = True
                for j in range(3):
                    if (left[i][j] + right[i-l-1][j]) < k:
                        good = False
                        break 
                if good: return True
            return False
        
        l, r = 0, len(s)
        while (l < r):
            mid = (l+r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1

        if check(l): return l
        if l == len(s): return -1
        return l + 1