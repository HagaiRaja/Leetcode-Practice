class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
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
        return ans