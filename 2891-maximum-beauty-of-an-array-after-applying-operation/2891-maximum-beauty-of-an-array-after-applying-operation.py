class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heap.append((num-k, 0))
            heap.append((num+k, 1))
        
        heap.sort()
        ans = 0
        score = 0
        for _, val in heap:
            if val: score -= 1
            else: score += 1
            ans = max(ans, score)
        return ans