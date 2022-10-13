class Solution:
    # hint
    # the valid tree -> no loop and the visit node is same with node number
    # make the adj table to run dfs -> this is the key skill(must be familiar)
    # https://www.youtube.com/watch?v=bXsUuownnoQ
    # 這題是沒有方向性的圖
    def validTree(self, n: int, edges: list) -> bool:
        # empty tree is valid tree
        if not n:
            return True

        # make a dictionary table
        adj = {i: [] for i in range(n)}

        # 做出每個node的之間相鄰關係
        # 這張preMap是沒有方向性的
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        print(adj)
        visit = set()

        # check loop case and add node into visit
        def dfs(i, prev):
            # base case
            if i in visit:
                return False

            visit.add(i)
            # 針對相鄰的node繼續往下走
            # 因為沒有方向性，所以碰到上一層node時要略過，可以跟leetcode 207比較
            # 往下走的模板
            for j in adj[i]:
                # 走過的node不能在走過
                if j == prev:
                    continue

                # normal case
                # 照到可以向下一層的node，把那個node當作下層
                prev = i
                if not dfs(j, prev):
                    return False
            return True

        # no loop and the visit node is same with node number
        # all of the node is start from 0 and we assume the prev is -1 when the start node is 0
        # print(dfs(0, -1) and n == len(visit))
        # dfs -> 判斷有無clcyle這件事情
        # n == len(visit) -> 判斷有node沒有相連
        return dfs(0, -1) and n == len(visit)

    # valid tree的圖形定義有2個
    # 1.Tree不能有cycle的情形發生
    # 2.當tree從起點走訪時，所有的node都會被走到，也就是說當中如果有node沒走到或者走過的node數量不是所有node的total就不是樹
    def validTree_2(self, n: int, edges: list) -> bool:
        def dfs(n, p):
            # base case
            if n in visit:
                return False

            visit.add(n)
            for item in graph_dict[n]:
                # 碰到上一層要略過，因為是無向圖，會這樣
                if item == p:
                    continue

                # 碰到cycle
                # n為下一個點的prev
                if not dfs(item, n):
                    return False

            # 這邊就不需要visit.remove了 -> 因為就是要統計走訪的node，所以回上層也不需要remove

            return True

        # 建立無向圖
        graph_dict = {}
        for i in range(n):
            graph_dict[i] = []

        # **對於建立無向圖不是很熟**
        for item in edges:
            graph_dict[item[0]].append(item[1])
            graph_dict[item[1]].append(item[0])

        visit = set()
        # **prev是用來記錄走過上層的node,下層就不能再走 -> 為無向圖的特殊技巧**
        node = 0
        prev = -1

        # 使用dfs來判斷是否有cycle
        return dfs(node, prev) and len(visit) == n


if __name__ == '__main__':
    solution = Solution()
    solution.validTree(n=5, edges=[[0,1],[0,2],[0,3],[0,4]])
    # solution.validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]])
    # 為clcyle的圖形
    # solution.validTree(n=3, edges=[[0, 1], [1, 2], [2, 0]])
    # 為visit node is same with node number
    # solution.validTree(n=6, edges=[[0, 1], [0, 2], [0, 3], [4, 5]])
