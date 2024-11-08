class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        allxor = 0
        for num in nums:
            allxor ^= num

        def add_k(cur):
            curb = bin(cur)[2:]
            if len(curb) >= maximumBit:
                curb = curb[-maximumBit:]
            else:
                curb = "0"*(maximumBit-len(curb)) + curb
            newb = ""
            for c in curb:
                if c == "0": newb += "1"
                else: newb += "0"
            return int(newb, 2)
        
        ans = []
        for i in range(len(nums)-1, -1, -1):
            ans.append(add_k(allxor))
            allxor ^= nums[i]
        return ans