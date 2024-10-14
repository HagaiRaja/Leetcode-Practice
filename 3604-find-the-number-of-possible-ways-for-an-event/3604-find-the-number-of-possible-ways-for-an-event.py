class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        MOD = 10**9 + 7

        dp = [[-1]*(min(n, x)+1) for _ in range(n+1)]
        def getStirling(n,k):
            if n < k: return 0
            if k == 1: return 1
            if dp[n][k] == -1:
                dp[n][k] = (getStirling(n-1, k-1) + k*getStirling(n-1, k)) % MOD
            return dp[n][k]

        def pow_mod(a, b): # a ** b
            cur = a
            ans = 1
            temp = b
            while (b):
                if b & 1:
                    ans *= cur
                    ans %= MOD
                cur *= cur
                cur %= MOD
                b >>= 1
            print("pow", a, temp, ans)
            return ans
        
        def perm(a,b):
            ans = 1
            for i in range(a,(a-b),-1):
                ans *= i
                ans %= MOD
            return ans
        
        ans = 0
        for num_band in range(1, min(n,x)+1):
            ans += getStirling(n, num_band)*perm(x, num_band)*pow_mod(y, num_band)
            print(num_band, getStirling(n, num_band), perm(x, num_band), pow_mod(y, num_band))
            ans %= MOD
        return ans