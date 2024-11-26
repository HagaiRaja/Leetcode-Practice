class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        # cleaning result
        clean = [items[0]]
        for p, b in items:
            pl, bl = clean.pop()
            if pl == p:
                clean.append([pl,b])
            else:
                clean.append([pl, bl])
                if b > bl:
                    clean.append([p, b])
        
        # binary search
        ans = []
        for q in queries:
            l, r = 0, len(clean) - 1
            while l < r:
                mid = (l+r) // 2
                if clean[mid][0] > q:
                    r = mid - 1
                elif clean[mid][0] < q:
                    l = mid + 1
                else:
                    l = mid
                    break

            if clean[l][0] > q: l -= 1

            if l == -1: ans.append(0)
            else: ans.append(clean[l][1]) 
        
        return ans