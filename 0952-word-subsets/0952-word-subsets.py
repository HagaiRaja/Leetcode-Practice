class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        min_chars = defaultdict(int)
        for word in words2:
            cnt = Counter(word)
            for c in cnt:
                min_chars[c] = max(min_chars[c], cnt[c])

        ans = []
        for word in words1:
            cnt = Counter(word)
            good = True
            for c in min_chars:
                if cnt[c] < min_chars[c]:
                    good = False
                    break
            if good: ans.append(word)
        return ans