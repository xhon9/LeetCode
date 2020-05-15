class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        ptr = self.root
        for i in word:
            if i not in ptr:
                ptr[i] = {}
            ptr = ptr[i]
        ptr['$'] = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for i in word:
            if i not in ptr:
                return False
            ptr = ptr[i]
        return '$' in ptr

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for i in prefix:
            if i not in ptr:
                return False
            ptr = ptr[i]
        return True
