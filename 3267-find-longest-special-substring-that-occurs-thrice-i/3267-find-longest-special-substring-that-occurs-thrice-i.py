class Solution:
    def maximumLength(self, s: str) -> int:
        def check(val):
            found = defaultdict(int)
            cnt = {}
            for i in range(val):
                if s[i] not in cnt: cnt[s[i]] = 0
                cnt[s[i]] += 1
            
            if len(cnt) == 1: found[list(cnt.keys())[0]] += 1
            for i in range(val, len(s)):
                if s[i] not in cnt: cnt[s[i]] = 0
                cnt[s[i]] += 1
                cnt[s[i-val]] -= 1
                if cnt[s[i-val]] == 0: del cnt[s[i-val]]
                if len(cnt) == 1: found[list(cnt.keys())[0]] += 1
            
            for val in found.values():
                if val >= 3: return True
            return False
        
        l, r = 1, len(s)
        while l < r:
            mid = (l+r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1

        if check(l): return l
        if l == 1: return -1
        return l - 1
