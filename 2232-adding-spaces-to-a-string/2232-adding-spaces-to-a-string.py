class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_s = ""
        i = 0
        for idx, c in enumerate(s):
            if i < len(spaces) and spaces[i] == idx:
                new_s += " "
                i += 1
            new_s += c
        return new_s