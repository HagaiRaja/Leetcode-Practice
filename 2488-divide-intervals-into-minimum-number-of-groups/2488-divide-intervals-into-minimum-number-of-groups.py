class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        group = []
        heapq.heapify(group)

        for l, r in intervals:
            if len(group):
                earliest_end = heapq.heappop(group)
                if earliest_end >= l:
                    heapq.heappush(group, earliest_end)
                heapq.heappush(group, r)
            else:
                heapq.heappush(group, r)
        return len(group)