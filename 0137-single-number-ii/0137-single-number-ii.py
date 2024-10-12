class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = [0]*32
        for num in nums:
            for i in range(32):
                if num & 1:
                    cnt[i] += 1
                num >>= 1
        # build ans
        ans = 0
        cur = 1
        for i in range(31):
            if cnt[i]%3:
                ans += cur
            cur <<= 1

        if cnt[31]%3:
            return ans - (1 << 31)
        return ans