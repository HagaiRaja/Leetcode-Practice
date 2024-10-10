class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k, ch, dup = 1, nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] == ch:
                if dup < 2:
                    nums[k] = ch
                    k += 1
                    dup += 1
            else:
                ch = nums[i]
                dup = 1
                nums[k] = ch
                k += 1
        return k