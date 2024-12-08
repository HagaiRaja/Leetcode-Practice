class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        times = []
        for s, e, v in events:
            times.append([s, 1, v])
            times.append([e+1, 0, v])
        
        ans, max_val = 0, 0
        times.sort()

        for t, is_start, v in times:
            if is_start:
                ans = max(ans, v + max_val)
            else:
                max_val = max(max_val, v)
        
        return ans