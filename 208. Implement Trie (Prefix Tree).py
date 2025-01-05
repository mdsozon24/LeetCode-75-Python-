class node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = node()

    def insert(self, word: str) -> None:
        crr = self.root

        for c in word:
            if c not in crr.children:
                crr.children[c] = node()
            crr = crr.children[c]
        crr.end = True

    def search(self, word: str) -> bool:
        crr = self.root

        for c in word:
            if c not in crr.children:
                return False
            crr = crr.children[c]
        return crr.end

    def startsWith(self, prefix: str) -> bool:
        crr = self.root

        for c in prefix:
            if c not in crr.children:
                return False
            crr = crr.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)