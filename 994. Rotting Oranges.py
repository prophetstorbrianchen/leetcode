import collections


class Solution:
    # hint
    # BFS -> 此題在求BFS中的queue level
    # https://www.youtube.com/watch?v=eZLK3WmDWq8
    def orangesRotting(self, grid: [[int]]) -> int:
        # 邊界
        rows = len(grid)
        cols = len(grid[0])

        # 把壞掉的放入queue中
        rot_list = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rot_list.append((row, col, 0))

        # rot_list做成deque
        q = collections.deque(rot_list)
        # 被加入過queue中的表示已經算過，不必再重算一次 -> 這是BFS必定使用的膜版
        seen = set(rot_list)

        # BFS
        d = 0
        while q:
            print(grid)
            i, j, d = q.popleft()
            # 往四個方向做BFS
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in seen:
                    # 開始感染好的
                    if grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        q.append((ni, nj, d + 1))
                        seen.add((ni, nj))

        if any(1 in row for row in grid):
            return -1

        print(d)
        return d


if __name__ == '__main__':
    solution = Solution()
    solution.orangesRotting(grid =[[1,2]])