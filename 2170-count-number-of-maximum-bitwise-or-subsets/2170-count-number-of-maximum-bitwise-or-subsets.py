class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = defaultdict(int)

        def backtrack(i, val):
            if i == len(nums):
                res[val] += 1
                return
            backtrack(i+1, val)
            backtrack(i+1, val|nums[i])
        backtrack(0, 0)

        max_val = 0
        for val in res:
            if val > max_val:
                max_val = val
        return res[max_val]