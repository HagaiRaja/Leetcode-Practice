class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        cnt = 0
        ch = word[0]

        for c in word:
            if c == ch:
                if cnt < 9:
                    cnt += 1
                else:
                    comp += "9" + ch
                    cnt = 1
            else:
                comp += f"{cnt}{ch}"
                ch = c
                cnt = 1
        comp += f"{cnt}{ch}"
        return comp
