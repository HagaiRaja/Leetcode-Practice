class TrieNode:
    def __init__(self, end=False):
        self.end = end
        self.next = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode(True)
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.next:
                cur.next[c] = TrieNode()
            cur = cur.next[c]
        cur.end = True

    def search(self, word: str) -> bool:
        queue = []
        queue.append((self.root, 0))
        while(queue):
            cur, i = queue.pop(0)
            if (i == len(word)):
                if (cur.end):
                    return True
            elif (word[i] == "."):
                for c in cur.next:
                    queue.append((cur.next[c], i+1))
            else:
                if (word[i] in cur.next):
                    queue.append((cur.next[word[i]], i+1))
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)