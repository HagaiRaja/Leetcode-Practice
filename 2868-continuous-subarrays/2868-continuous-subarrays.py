class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        min_heap = []
        max_heap = []
        l, r = 0, 0
        count = 0

        while r < len(nums):
            heapq.heappush(min_heap, (nums[r], r))
            heapq.heappush(max_heap, (-nums[r], r))
            
            while l < r and (-max_heap[0][0] - min_heap[0][0]) > 2:
                l += 1

                while min_heap and min_heap[0][1] < l:
                    heapq.heappop(min_heap)
                while max_heap and max_heap[0][1] < l:
                    heapq.heappop(max_heap)
                
            count += r - l + 1
            r += 1
        
        return count