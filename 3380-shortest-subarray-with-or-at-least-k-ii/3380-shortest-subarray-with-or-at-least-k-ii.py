class XorSum:
    def __init__(self):
        self.cnt = [0]*32
    
    def getVal(self):
        val = ""
        for num in reversed(self.cnt):
            if num > 0: val += "1"
            else: val += "0"
        return int(val, 2)
    
    def insert(self, val):
        pos = 0
        while val:
            if val & 1:
                self.cnt[pos] += 1
            val >>= 1
            pos += 1
    
    def remove(self, val):
        pos = 0
        while val:
            if val & 1:
                self.cnt[pos] -= 1
            val >>= 1
            pos += 1

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        val = XorSum()
        ans = len(nums) + 1
        while r < len(nums):
            val.insert(nums[r])
            if val.getVal() >= k:
                while l < r:
                    val.remove(nums[l])
                    if val.getVal() < k:
                        val.insert(nums[l])
                        break
                    l += 1
                ans = min(ans, r-l+1)
            r += 1
        if ans == (len(nums) + 1): return -1
        return ans