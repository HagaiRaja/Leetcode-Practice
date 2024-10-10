class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, total = 0, 0, 0
        ans = len(nums)
        while r < len(nums):
            total += nums[r]
            while total >= target:
                ans = min(r-l+1, ans)
                if total - nums[l] < target: break
                total -= nums[l]
                l += 1
            r += 1
        
        if ans == len(nums) and total < target: return 0
        return ans