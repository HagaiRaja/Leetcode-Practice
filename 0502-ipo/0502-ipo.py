class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        combo = []
        for i in range(len(profits)):
            combo.append([capital[i], profits[i]])
        combo.sort()

        avail = []
        heapq.heapify(avail)
        combo_i = 0
        while k > 0:
            # adjust project that can be done
            while combo_i < len(combo) and combo[combo_i][0] <= w:
                heapq.heappush(avail, -combo[combo_i][1])
                combo_i += 1
            # pick best project
            if len(avail):
                cur_cap = heapq.heappop(avail)
                w -= cur_cap # I multiply by -1 before
            k -= 1
        return w