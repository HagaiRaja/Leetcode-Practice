class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        def get_min_idx():
            min_i = 0
            for i in range(1, len(nums)):
                if nums[i] < nums[min_i]: min_i = i
            return min_i

        for _ in range(k):
            i = get_min_idx()
            nums[i] *= multiplier
        
        return nums