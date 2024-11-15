class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        r = len(arr) - 1
        while r > 0 and arr[r] >= arr[r-1]:
            r -= 1
        
        ans = r
        l = 0
        while l < r and (l == 0 or arr[l-1] <= arr[l]):
            while r < len(arr) and arr[l] > arr[r]:
                r += 1
            ans = min(ans, r-l-1)
            l += 1
        return ans