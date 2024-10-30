class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)

        l = [1]*N
        r = [1]*N

        # increasing
        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j]:
                    l[i] = max(l[i], l[j] + 1)
        # decreasing
        for i in range(N-1, -1, -1):
            for j in range(N-1, i, -1):
                if nums[i] > nums[j]:
                    r[i] = max(r[i], r[j] + 1)
        # search ans
        # print(l)
        # print(r)
        ans = N
        for i in range(1, N-1):
            if l[i] == 1 or r[i] == 1: continue
            ans = min(ans, N-l[i]-r[i]+1)
            # print(i, N-l[i]-r[i]+1)
        return ans
        