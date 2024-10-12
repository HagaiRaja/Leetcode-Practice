class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        if len(nums) == 2:
            if nums[0] > nums[1]: return 0
            else: return 1

        l, r = 0, len(nums)-1

        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[mid-1]:
                if nums[mid] > nums[mid+1]:
                    return mid
                else:
                    l = mid + 1
            else:
                if nums[mid] > nums[mid+1]:
                    r = mid - 1
                else:
                    l = mid + 1
        return l
            