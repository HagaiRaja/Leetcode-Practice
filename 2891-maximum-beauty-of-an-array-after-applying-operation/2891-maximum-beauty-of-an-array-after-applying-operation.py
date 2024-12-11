class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, (num-k, 0))
            heapq.heappush(heap, (num+k, 1))
        
        ans = 0
        score = 0
        while len(heap):
            _, val = heapq.heappop(heap)
            if val: score -= 1
            else: score += 1
            ans = max(ans, score)
        return ans