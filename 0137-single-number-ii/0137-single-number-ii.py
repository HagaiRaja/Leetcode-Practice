class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        fi, se = set(), set()
        ans = 0
        for num in nums:
            if num in se: continue
            if num in fi:
                se.add(num)
            else:
                fi.add(num)
            ans ^= num
        return ans