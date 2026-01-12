class Node:
    
    def __init__(self):
        self.wordMap: dict[str, Node] = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c in node.wordMap:
                node = node.wordMap[c]
            else:
                child = Node()
                node.wordMap[c] = child
                node = child
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.wordMap:
                return False
            node = node.wordMap[c]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.wordMap:
                return False
            node = node.wordMap[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)