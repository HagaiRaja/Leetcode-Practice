class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        half = len(nums)/2
        for num in cnt:
            if cnt[num] > half:
                return num