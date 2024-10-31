class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        cache = {}
        def backtrack(r, f):
            if r == len(robot): return 0
            if f == len(factory): return 10**12
            key = (r,f,factory[f][1])
            if key in cache: return cache[key]
            # skip this factory
            ans = backtrack(r, f+1)
            if factory[f][1] > 0: # can repair
                factory[f][1] -= 1
                ans = min(ans, abs(robot[r]-factory[f][0]) + backtrack(r+1, f))
                factory[f][1] += 1
            cache[key] = ans
            return ans
        return backtrack(0, 0)
