class TireNode:
    def __init__(self):
        self.children = {}
        self.endOfNode = False


class Trie:
    # hint
    # 要熟記TireNode
    # 必須要熟練insert和search
    def __init__(self):
        # 初始root為空
        self.root = TireNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TireNode()
            cur = cur.children[c]
        cur.endOfNode = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False

        if cur.endOfNode is True:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False

        return True

    def insert_2(self, word: str) -> None:
        cur = self.root

        for c in word:
            # **因為是insert，有找到那就往下層走，沒找到那就建TireNode()，在繼續往下走**
            if c not in cur.children:
                cur.children[c] = TireNode()
            cur = cur.children[c]
        cur.endOfNode = True

    def search_2(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c in cur.children:
                # **往下層走**
                cur = cur.children[c]
            else:
                return False

        if cur.endOfNode:
            return True
        else:
            return False

    def startsWith_2(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))