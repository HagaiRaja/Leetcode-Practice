class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sums = 0
        cnt = {}

        for i in range(k):
            sums += nums[i]
            if nums[i] not in cnt: cnt[nums[i]] = 0
            cnt[nums[i]] += 1
        
        if len(cnt) == k: ans = sums
        else: ans = 0

        for i in range(k, len(nums)):
            cnt[nums[i-k]] -= 1
            sums -= nums[i-k]
            if nums[i] not in cnt: cnt[nums[i]] = 0
            cnt[nums[i]] += 1
            sums += nums[i]
            if cnt[nums[i-k]] == 0:
                del cnt[nums[i-k]]
            if len(cnt) == k: ans = max(ans, sums)

        return ans