class TrieNode:
    def __init__(self):
        self.sub = [None] * 26
        self.end = False

class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        t = self.trie
        for char in word:
            index = ord(char) - ord('a')
            if t.sub[index] is None:
                t.sub[index] = TrieNode()
            t = t.sub[index]
        t.end = True

    def search(self, word: str) -> bool:
        t = self.trie
        for char in word:
            index = ord(char) - ord('a')
            if t.sub[index] is None:
                return False
            t = t.sub[index]
        return t.end

    def startsWith(self, prefix: str) -> bool:
        t = self.trie
        for char in prefix:
            index = ord(char) - ord('a')
            if t.sub[index] is None:
                return False
            t = t.sub[index]
        return True