class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(nums) - k + 1):
            mx = nums[i]
            isSort = True
            for j in range(i+1, i+k):
                if (nums[j] - 1) != nums[j-1]:
                    isSort = False
                    break
                else:
                    mx = max(mx, nums[j])
            if isSort:
                ans.append(mx)
            else:
                ans.append(-1)
        return ans