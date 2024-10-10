class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [0]
        for i in range(1, len(nums)):
            if nums[stack[-1]] > nums[i]:
                stack.append(i)
        
        # compare
        ans = 0
        for i in range(len(nums)-1, -1, -1):
            while len(stack) and nums[stack[-1]] <= nums[i]:
                ans = max(ans, i-stack[-1])
                stack.pop()
        return ans