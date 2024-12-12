class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] *= -1
        heapq.heapify(gifts)

        for _ in range(k):
            cur = heapq.heappop(gifts)
            heapq.heappush(gifts, -int((cur*-1)**0.5))
        return sum(gifts)*-1