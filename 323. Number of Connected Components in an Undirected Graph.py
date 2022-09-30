class Solution:
    # hint
    # Union Find的演算法
    # 這題還是不懂，需要多看幾次，這題的觀念很重要
    # 多看筆記和影片
    # https://www.youtube.com/watch?v=8f1XPm4WOUc
    def countComponents(self, n: int, edges: list) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res= n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] = rank[p2] + rank[p1]
            else:
                par[p2] = p1
                rank[p1] = rank[p1] + rank[p2]

            return 1

        res = n
        for n1, n2 in edges:
            res = res - union(n1, n2)

        return res


if __name__ == '__main__':
    solution = Solution()
    solution.countComponents(n=5, edges = [[0,1],[1,2],[3,4]])