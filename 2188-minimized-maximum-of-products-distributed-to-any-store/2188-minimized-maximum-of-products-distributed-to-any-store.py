class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check(split):
            m = 0
            for q in quantities:
                m += q//split + ((q%split) != 0)
            return m <= n
        
        l, r = 1, max(quantities)
        while (l < r):
            mid = (l+r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        if check(l): return l
        return l + 1