import collections


class Solution:
    # https://hackmd.io/@alan25sprout/S1Yjq9RUO
    def keyboard_time_bfs(self, s: str, keyboard: str):
        # --method 1 bfs--
        # bfs function
        def bfs(r, c, m, t):
            q = collections.deque()
            seen = set()

            q.append((r, c, 0))
            seen.add((r, c))

            # 上/右上/右/右下/下/左下/左/左上
            directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

            while q:
                in_row, in_col, cost_time = q.popleft()
                # 找到target value
                if m[in_row][in_col] == t:
                    return cost_time

                for tmp_r, tmp_c in directions:
                    if 0 <= in_row + tmp_r < len(matric) and 0 <= in_col + tmp_c < len(matric[0]) and (in_row + tmp_r, in_col + tmp_c) not in seen:
                        q.append((in_row + tmp_r, in_col + tmp_c, cost_time + 1))
                        seen.add((in_row + tmp_r, in_col + tmp_c))

        # transfer the keyboard from string to 2D list
        matric = []
        tmp = []
        for n in keyboard:
            tmp.append(n)
            if len(tmp) == 3:
                matric.append(tmp)
                tmp = []

        # get total rows and cols
        rows = len(matric)
        cols = len(matric[0])

        total_time = 0
        for i, number in enumerate(s):
            # prevent out of list index
            if i + 1 == len(s):
                break

            flag = False
            for r in range(rows):
                for c in range(cols):
                    if matric[r][c] == number:
                        time = bfs(r, c, matric, s[i + 1])
                        # print("start", matric[r][c], "end", s[i + 1], "time", time)
                        total_time = total_time + time
                        flag = True
                if flag:
                    break

        # print(total_time)
        return total_time

    # --method 2 hash table--
    def keyboard_time_hash_table(self, s: str, keyboard: str):
        pass


if __name__ == '__main__':
    solution = Solution()
    s = "5111"
    keyboard = "752961348"
    solution.keyboard_time_bfs(s, keyboard)