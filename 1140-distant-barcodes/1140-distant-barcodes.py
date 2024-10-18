class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = Counter(barcodes)
        pq = []
        for k in cnt:
            pq.append([-cnt[k], k])
        heapq.heapify(pq)

        ans = [-1]
        while len(pq):
            occ, num = heapq.heappop(pq)
            if num == ans[-1]:
                occ1, num1 = heapq.heappop(pq)
                ans.append(num1)
                occ1 += 1
                if occ1: heapq.heappush(pq, [occ1, num1])
            ans.append(num)
            occ += 1
            if occ: heapq.heappush(pq, [occ, num])
        return ans[1:]