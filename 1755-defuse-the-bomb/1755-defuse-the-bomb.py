class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        ans = [0]*N
        if k == 0: return ans
        code += code
        for i in range(N):
            if k > 0:
                ans[i] = sum(code[i+1:i+k+1])
            else:
                ans[i] = sum(code[N+i+k:N+i])
        return ans