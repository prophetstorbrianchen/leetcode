import collections


class Solution:
    # hint
    # https://www.youtube.com/watch?v=xPksuvWKzqg
    # https://maxming0.github.io/2020/11/04/Minimum-Height-Trees/
    def findMinHeightTrees(self, n: int, edges: [[int]]) -> [int]:
        edge = [set() for _ in range(n)]

        # 製作無向圖
        for u, v in edges:
            edge[u].add(v)
            edge[v].add(u)

        # 找入度為1的點 -> 即為leaf node
        # q = [x for x in range(n) if len(edge[x]) < 2]
        q = []
        for x in range(n):
            if len(edge[x]) < 2:
                q.append(x)

        tmp = []
        # 把所以度為1的leaf node和邊去掉 -> 更新完之後為新的一張圖在重複一次這個動作，直到剩下來的node度為1
        while True:
            # 準備移除leaf node
            for node in q:
                # 把所以度為1的leaf node和邊去掉
                for n in edge[node]:
                    edge[n].remove(node)
                    # 度為1的node
                    if len(edge[n]) == 1:
                        tmp.append(n)
            if not tmp:
                break

            # 砍完了node和edge，重新更新一次圖，在跑一次loop
            tmp, q = [], tmp

        print(q)
        return q

    def findMinHeightTrees_2(self, n: int, edges: [[int]]) -> [int]:
        # Topological Sort的題目基本上都離不開幾點 -> indegree/outdegree/dfs/bfs/ACG/cycle
        # 這題算是特殊提，問拿那些node才會是min high tree -> 把邊和node去掉之後，剩下入度為1的node，即是答案
        # 這題應該還有更好理解的方法還有coding方式 -> 需要再找過

        edge = collections.defaultdict(set)

        # 製作無向圖
        for u, v in edges:
            edge[u].add(v)
            edge[v].add(u)

        # 找入度點為1的，即是len(edges)只有1的node -> 也就是leaf node
        q = []
        for key, value in edge.items():
            if len(value) == 1:
                q.append(key)

        tmp = []
        # 把所以度為1的leaf node和邊去掉 -> 更新完之後為新的一張圖在重複一次這個動作，直到剩下來的node度為1
        while True:
            # 準備移除leaf node
            for node in q:
                # 把所以度為1的leaf node和邊去掉
                for n in edge[node]:
                    edge[n].remove(node)
                    # 度為1的node
                    if len(edge[n]) == 1:
                        tmp.append(n)
            if not tmp:
                break

            # 砍完了node和edge，重新更新一次圖，在跑一次loop
            tmp, q = [], tmp

        print(q)
        return q


if __name__ == '__main__':
    solution = Solution()
    solution.findMinHeightTrees_2(n = 4, edges = [[1,0],[1,2],[1,3]])