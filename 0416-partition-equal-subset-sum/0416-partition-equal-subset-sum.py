class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1: return False
        target = total//2

        dp = set([0])
        for num in nums:
            for val in list(dp):
                if val+num == target:
                    return True
                dp.add(val+num)
        return False