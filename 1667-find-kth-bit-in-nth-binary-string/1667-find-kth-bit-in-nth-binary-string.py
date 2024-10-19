class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1: return "0"

        cur = 1 << n

        if k > (cur >> 1):
            return "1" if self.findKthBit(n-1, cur-k) == "0" else "0"
        elif k < (cur >> 1):
            return self.findKthBit(n-1, k)
        else:
            return "1"

            # "0111001 1 0110001"
            #. 0123456 7 8901234