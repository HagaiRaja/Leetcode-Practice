class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        maxR = nums[0][0]
        ans = [-10**5, 10**5]
        for i in range(len(nums)):
            heapq.heappush(pq, [nums[i][0], i, 0])
            maxR = max(maxR, nums[i][0])
        
        while True:
            val, i, j = heapq.heappop(pq)
            if (maxR-val) < (ans[1]-ans[0]):
                ans = [val, maxR]
            j += 1
            if j == len(nums[i]): break
            heapq.heappush(pq, [nums[i][j], i, j])
            maxR = max(maxR, nums[i][j])
        return ans