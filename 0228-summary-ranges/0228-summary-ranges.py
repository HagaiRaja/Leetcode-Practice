class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: return []
        ans = []
        start, end = nums[0], nums[0]
        for i in range(1, len(nums)):
            if (nums[i] - end) == 1:
                end += 1
            else:
                if start == end:
                    ans.append(f"{start}")
                else:
                    ans.append(f"{start}->{end}")
                start, end = nums[i], nums[i]

        if start == end:
            ans.append(f"{start}")
        else:
            ans.append(f"{start}->{end}")
        return ans