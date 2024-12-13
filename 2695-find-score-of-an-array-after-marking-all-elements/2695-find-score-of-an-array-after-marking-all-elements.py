class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(heap)
        mark = [False]*len(heap)

        score = 0
        while len(heap):
            val, idx = heapq.heappop(heap)
            if mark[idx]: continue
            mark[idx] = True
            if idx > 0: mark[idx-1] = True
            if idx < (len(nums) - 1): mark[idx+1] = True
            score += val
        return score