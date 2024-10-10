class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def merge(l, r):
            if r == l: return words[l] + ( " "*( maxWidth-len(words[l]) ) )
            min_len = sum([len(words[i]) for i in range(l, r+1)])
            total_space = maxWidth - min_len
            min_space = total_space // (r-l)
            left_space = total_space % (r-l)
            res = words[l]
            for i in range(l+1, r+1):
                res += " "*min_space
                if left_space:
                    res += " "
                    left_space -= 1
                res += words[i]
            return res

        ans = []
        l, r, total_ch = 0, 1, len(words[0])
        while r < len(words):
            if total_ch + len(words[r]) + 1 > maxWidth:
                # process
                ans.append(merge(l, r-1))
                l = r
                total_ch = len(words[r])
            else:
                total_ch += len(words[r]) + 1
            r += 1
        final = " ".join(words[l:])
        ans.append(final + ( " "*( maxWidth-len(final) ) ))
        return ans