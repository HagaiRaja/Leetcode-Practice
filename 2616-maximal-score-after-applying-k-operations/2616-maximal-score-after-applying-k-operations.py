class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        ans = 0
        for _ in range(k):
            cur = heapq.heappop(nums)
            cur *= -1
            ans += cur
            ne = cur//3
            if cur%3: ne += 1
            heapq.heappush(nums, ne*-1)
        return ans