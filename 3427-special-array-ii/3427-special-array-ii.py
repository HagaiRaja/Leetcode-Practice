class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        bads = [0]*len(nums)
        for i in range(1, len(nums)):
            if (nums[i] & 1) == (nums[i-1] & 1):
                bads[i] = bads[i-1] + 1
            else:
                bads[i] = bads[i-1]

        ans = []
        for s, e in queries:
            if bads[e] - bads[s]:
                ans.append(False)
            else:
                ans.append(True)
        return ans