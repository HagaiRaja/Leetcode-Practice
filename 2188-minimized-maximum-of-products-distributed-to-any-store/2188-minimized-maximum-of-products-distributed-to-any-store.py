class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        heap = [(-q, 1) for q in quantities]
        heapq.heapify(heap)

        for _ in range(n-len(quantities)):
            q, num = heapq.heappop(heap)
            q = (q*num)/(num+1)
            heapq.heappush(heap, (q, num+1))
        
        q, num = heapq.heappop(heap)
        q *= -1
        return int(q) + ((q - int(q)) != 0)
