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



    def updateMatrix_2(self, mat: [[int]]) -> [[int]]:
        # 這題比較特別，要建立一張新的表都是0的matrix -> 用來計算1的count -> 這方法其實非常常用到(多練習)
        # 必須將0加入queue中開始向4方擴散 -> 找到1，就更新在新的表格上面，做累加的動作

        # 土法煉鋼法
        """
        dict = []
        for i in range(len(mat)):
            tmp = []
            for j in range(len(mat[0])):
                tmp.append(0)
            dict.append(tmp)
        """

        # 乾淨寫法
        m, n = len(mat), len(mat[0])
        dict = [[0] * n for _ in range(m)]


        # 找是0的位置，放入queue中
        zeroes_pos = []
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    zeroes_pos.append((r, c))

        q = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)

        # BFS
        # 更新dict的內容
        while q:
            r, c = q.popleft()
            # 4方擴散
            # 上
            if 0 <= r - 1 < m and 0 <= c < n and (r - 1, c) not in seen:
                # 因為0都已經被挑到queue裡面了，所以剩餘的mat中必定為1
                # mat[i][j] is either 0 or 1 -> 題目有限制
                dict[r - 1][c] = dict[r][c] + 1
                q.append((r - 1, c))
                seen.add((r - 1, c))

            # 下
            if 0 <= r + 1 < m and 0 <= c < n and (r + 1, c) not in seen:
                dict[r + 1][c] = dict[r][c] + 1
                q.append((r + 1, c))
                seen.add((r + 1, c))

            # 左
            if 0 <= r < m and 0 <= c - 1 < n and (r, c - 1) not in seen:
                dict[r][c - 1] = dict[r][c] + 1
                q.append((r, c - 1))
                seen.add((r, c - 1))

            # 右
            if 0 <= r < m and 0 <= c + 1 < n and (r, c + 1) not in seen:
                dict[r][c + 1] = dict[r][c] + 1
                q.append((r, c + 1))
                seen.add((r, c + 1))

        print(dict)
        return dict


if __name__ == '__main__':
    solution = Solution()
    solution.updateMatrix_2(mat = [[0,0,0],[0,1,0],[1,1,1]])