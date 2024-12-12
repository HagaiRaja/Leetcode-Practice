class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        stack = [-i for i in gifts]
        heapq.heapify(stack)

        for _ in range(k):
            cur = heapq.heappop(stack)
            heapq.heappush(stack, -int((cur*-1)**0.5))
        return sum(stack)*-1