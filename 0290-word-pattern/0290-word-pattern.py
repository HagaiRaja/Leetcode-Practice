class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s): return False
        s_tab, p_tab = {}, {}
        for i in range(len(pattern)):
            if pattern[i] in p_tab:
                if p_tab[pattern[i]] != s[i]: return False
            else:
                p_tab[pattern[i]] = s[i]

            if s[i] in s_tab:
                if s_tab[s[i]] != pattern[i]: return False
            else:
                s_tab[s[i]] = pattern[i]
        return True