class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        cnt = defaultdict(set)

        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                if (points[i][0]-points[j][0]) == 0:
                    m = float('inf')
                    c = points[i][0]
                else:
                    m = (points[i][1]-points[j][1]) / (points[i][0]-points[j][0])
                    c = points[i][1] - m*points[i][0]
                key = (m,c)
                cnt[key].add(i)
                cnt[key].add(j)
        ans = 1

        for m in cnt:
            ans = max(ans, len(cnt[m]))
        return ans