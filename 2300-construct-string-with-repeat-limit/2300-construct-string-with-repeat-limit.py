class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = Counter(s)
        heap = []

        for c in cnt:
            heapq.heappush(heap, (-ord(c), cnt[c]))
        
        ans = "@"
        while len(heap):
            ci, num = heapq.heappop(heap)
            c = chr(ci*-1)
            if c == ans[-1]:
                if not len(heap): break
                ci1, num1 = heapq.heappop(heap)
                ans += chr(ci1*-1)
                if num1 > 1: heapq.heappush(heap, (ci1, num1-1))
            
            if num > repeatLimit:
                ans += c*repeatLimit
                heapq.heappush(heap, (ci, num-repeatLimit))
            else:
                ans += c*num

        return ans[1:]