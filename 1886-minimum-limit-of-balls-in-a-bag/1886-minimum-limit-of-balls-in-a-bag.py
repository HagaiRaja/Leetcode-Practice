class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(target):
            total_operation = 0
            for num in nums:
                div = num // target
                mod = (num % target) > 0
                total_operation += div + mod - 1
                if total_operation > maxOperations: return False
            return True
        
        l, r = 1, max(nums)
        while l < r:
            mid = (l+r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l