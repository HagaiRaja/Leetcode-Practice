class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        temp = nums[len(nums)-k:]
        for i in range(len(nums)-1, k-1, -1):
            nums[i] = nums[i-k]
        for i in range(k):
            nums[i] = temp[i]