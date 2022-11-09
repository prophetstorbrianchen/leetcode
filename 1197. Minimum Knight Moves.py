import collections


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = collections.deque()
        q.append((0, 0, 0))
        direction = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, 1)]
        visited = set()
        visited.add((0, 0))

        # BFS模板
        while q:
            x_loc, y_loc, step = q.popleft()
            for tmp_x, tmp_y in direction:
                if 0 <= (x_loc + tmp_x) <= x and 0 <= (y_loc + tmp_y) <= y and ((x_loc + tmp_x), (y_loc + tmp_y)) not in visited:
                    if (x_loc + tmp_x) == x and (y_loc + tmp_y) == y:
                        print(step + 1)
                        return step + 1
                    else:
                        q.append(((x_loc + tmp_x), (y_loc + tmp_y), (step + 1)))
                        visited.add(((x_loc + tmp_x), (y_loc + tmp_y)))

        return -1


if __name__ == '__main__':
    solution = Solution()
    solution.minKnightMoves(x = 2, y = 1)