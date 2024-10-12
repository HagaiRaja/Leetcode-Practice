class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        print(nums)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue

            l, r = i + 1, len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1 
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1

        return ans