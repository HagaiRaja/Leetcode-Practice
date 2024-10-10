class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def check(mid):
            cnt = 0
            for cit in citations:
                if cit >= mid: cnt += 1
            return mid <= cnt

        l, r = 0, 1000
        while l < r:
            mid = (l+r)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        
        if check(l):
            return l
        return l-1