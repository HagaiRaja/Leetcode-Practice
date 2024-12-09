class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        bads = []
        for i in range(len(nums)-1):
            if (nums[i] & 1) == (nums[i+1] & 1):
                bads.append(i)

        def get_idx(val):
            l, r = 0, len(bads)
            while l < r:
                mid = (l+r)//2
                if bads[mid] > val:
                    r = mid
                elif bads[mid] < val:
                    l = mid + 1
                else:
                    l = mid
                    break
            return l

        ans = []
        for s, e in queries:
            s1 = get_idx(s)
            e1 = get_idx(e)
            if e1-s1 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans