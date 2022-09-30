class Solution:
    # hint
    # 這題很難，可以多用幾個例子來理解
    # 第一個部分是建立圖形，第二個是DFS利用dict去歷遍所有點
    # 要了解visited的True和False的意義
    # 要了解dfs所return的True和False的意義
    def alienOrder(self, words: list) -> str:
        adj = {char: set() for word in words for char in word}

        # 建表
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # ex: ["waf", "wa"] -> 這順序有問題,直接回空
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            # 如何把圖弄出來
            # 2個字開始比，若第一個就不一樣，做dict起來
            # ex: ["wrf", "er"] -> {w:set(e)}
            # ex: ["wrt", "wrf"] -> {t:set(f)}
            # 直到所有都做完
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # print(w1[j], w2[j])
                    adj[w1[j]].add(w2[j])
                    break

        # print(adj)

        visited = {}  # {char: bool} False visited, True current path
        res = []

        def dfs(char):
            # base case
            if char in visited:
                return visited[char]

            # 在current path
            visited[char] = True

            # 使用dict和dfs往下找
            for neighChar in adj[char]:
                # 若是回true，則表示碰到cycle
                if dfs(neighChar):
                    return True

            # 走訪過後，要把True轉為False
            visited[char] = False
            res.append(char)
            return False

        # 每隔char都找過一次
        for char in adj:
            # 若為True表示有cycle
            if dfs(char):
                return ""

        # 因為使用postorder dfs,從leaf往回
        res.reverse()
        print(res)
        return "".join(res)


if __name__ == '__main__':
    solution = Solution()
    solution.alienOrder(words=["wrt", "wrf", "er", "ett", "rftt"])
    # solution.alienOrder(words=["we", "ee", "we"])