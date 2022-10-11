class TireNode:
    def __init__(self):
        self.children = {}
        self.endOfNode = False


class WordDictionary:
    # hint
    # 這提是變化題
    # 理解了之後，code要多看，尤其在處理dfs的case上
    def __init__(self):
        # 初始root為空
        self.root = TireNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TireNode()
            cur = cur.children[c]
        cur.endOfNode = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            # 需分成2種case，有碰到"."和沒碰到"."
            # 沒碰到 -> 跟之前題目一樣，如果不再cur.children，就return False，如果有在cur.children，就往下層走
            # 有碰到 -> 走dfs，運用key, value，解析child，然後在往下帶
            for i in range(j, len(word)):
                c = word[i]
                # 碰到"." 要往下層走
                if c == ".":
                    # 往下一層有可能的char去做搜尋，i要加1，把child再往下帶(也就是往下層走的意思)
                    for char, child in cur.children.items():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    # 非"." 的case
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            # 想一想base case
            # 當只有一個node的時候會回甚麼 -> 用cur.endOfNode去回答True or False
            return cur.endOfNode

        # 從第0層開始，可以看我的筆記
        return dfs(0, self.root)





    def addWord_2(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TireNode()
            cur = cur.children[c]
        cur.endOfNode = True

    def search_2(self, word: str) -> bool:
        def dfs(layer, root):
            cur = root

            # **注意他是用layer來當c走到哪層**
            for index in range(layer, len(word)):
                c = word[index]
                if c == ".":
                    # **往下一層有可能的char去做搜尋，index要加1，把child再往下帶(也就是往下層走的意思)**
                    for key, value in cur.children.items():
                        if dfs(index + 1, value):
                            return True
                    return False
                else:
                    if c in cur.children:
                        cur = cur.children[c]
                    else:
                        return False

            return cur.endOfNode

        return dfs(0, self.root)


if __name__ == '__main__':
    worddictionary = WordDictionary()
    worddictionary.addWord("bad")
    worddictionary.addWord("dad")
    worddictionary.addWord("mad")
    worddictionary.search("pad")
    worddictionary.search("bad")
    worddictionary.search(".ad")
    worddictionary.search("b..")