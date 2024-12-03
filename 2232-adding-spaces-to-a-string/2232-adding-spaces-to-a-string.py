class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words = [s[0:spaces[0]]]
        for i in range(1, len(spaces)):
            words.append(s[spaces[i-1]:spaces[i]])
        words.append(s[spaces[-1]:len(s)])
        return " ".join(words)