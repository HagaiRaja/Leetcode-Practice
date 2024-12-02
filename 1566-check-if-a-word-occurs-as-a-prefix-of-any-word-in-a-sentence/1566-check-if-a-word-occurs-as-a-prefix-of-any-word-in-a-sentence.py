class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for idx, word in enumerate(sentence.split(" ")):
            if len(word) >= len(searchWord) and word[:len(searchWord)] == searchWord:
                return idx + 1
        return -1