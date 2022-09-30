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


if __name__ == '__main__':
    solution = Solution()
    solution.validTree(n=5, edges=[[0,1],[0,2],[0,3],[0,4]])
    # solution.validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]])
    # 為clcyle的圖形
    # solution.validTree(n=3, edges=[[0, 1], [1, 2], [2, 0])
    # 為visit node is same with node number
    # solution.validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [4, 5]])