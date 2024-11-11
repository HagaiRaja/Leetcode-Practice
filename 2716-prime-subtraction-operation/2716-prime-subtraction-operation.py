class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = {}
        def isPrime(num):
            if num in primes: return primes[num]
            prime = True
            for i in range(2, int(num**0.5)+1):
                if (num % i) == 0:
                    prime = False
                    break
            primes[num] = prime
            return prime
        
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]: continue
            p = 2
            found = False
            while p < nums[i-1]:
                if isPrime(p):
                    if (nums[i-1] - p) < nums[i]:
                        found = True
                        break
                p += 1
            if not found: return False
            nums[i-1] -= p
        return True