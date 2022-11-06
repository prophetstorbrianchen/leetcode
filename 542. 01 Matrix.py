import collections


class Solution:
    # hint
    # 這題跟大西洋太平洋那題很像 -> BFS的概念
    # 看答案看不懂沒關係，但要trace code去理解
    # https://leetcode.cn/problems/01-matrix/solution/01ju-zhen-by-leetcode-solution/
    def updateMatrix(self, mat: [[int]]) -> [[int]]:
        m, n = len(mat), len(mat[0])

        # dist為新的矩陣，先全部給0
        dist = [[0] * n for _ in range(m)]

        # 把zero的放入queue
        # zeroes_pos = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]
        zeroes_pos = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    zeroes_pos.append((i, j))

        # zeroes_pos的list做成deque
        q = collections.deque(zeroes_pos)
        # 被加入過queue中的表示已經算過，不必再重算一次 -> 這是BFS必定使用的膜版
        seen = set(zeroes_pos)

        # BFS
        while q:
            i, j = q.popleft()
            # 往四個方向做BFS
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                # 邊界外不看
                # 看過的不看
                # 只處理碰到1而且沒被看過的 -> 因為loop過後就會有碰到1但是是有處理過的(看過的)
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))

        print(dist)
        return dist


if __name__ == '__main__':
    solution = Solution()
    solution.updateMatrix(mat = [[0,0,0],[0,1,0],[1,1,1]])