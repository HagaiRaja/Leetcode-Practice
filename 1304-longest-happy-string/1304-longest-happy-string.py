class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        heapq.heapify(pq)
        if a: heapq.heappush(pq, [-a, "a"])
        if b: heapq.heappush(pq, [-b, "b"])
        if c: heapq.heappush(pq, [-c, "c"])

        ans = "d"
        while len(pq):
            occ, ch = heapq.heappop(pq)
            if ch == ans[-1] and len(pq):
                occ1, ch1 = heapq.heappop(pq)
                if occ1*2 >= (occ-1) or occ1 == -1:
                    ans += ch1
                    occ1 += 1
                else:
                    ans += ch1*2
                    occ1 += 2
                if occ1 != 0:
                    heapq.heappush(pq, [occ1, ch1])

            if ch != ans[-1]:
                if occ < -1:
                    ans += ch*2
                    occ += 2
                else:
                    ans += ch
                    occ += 1
                if occ != 0:
                    heapq.heappush(pq, [occ, ch])
        return ans[1:]

"""
ccbbccbb
4
7
cc bb

cc b cc b c
"""