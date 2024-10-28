class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        mapp = {}
        ans = 1
        for num in nums:
            if num*num in mapp:
                mapp[num] = mapp[num*num] + 1
                ans = max(ans, mapp[num])
            else:
                mapp[num] = 1
        if ans == 1: return -1
        return ans