class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def count_bits(num):
            cnt = 0
            while num:
                cnt += (num & 1)
                num >>= 1
            return cnt
        
        prevMax = 0
        i = 0
        while i < len(nums):
            curMax, curMin = nums[i], nums[i]
            curBit = count_bits(nums[i])
            i += 1
            while i < len(nums):
                curBit1 = count_bits(nums[i])
                if curBit == curBit1:
                    curMax = max(nums[i], curMax)
                    curMin = min(nums[i], curMin)
                    i += 1
                else:
                    break
            if curMin < prevMax: return False
            prevMax = curMax

        return True