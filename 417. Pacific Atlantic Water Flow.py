class Solution:
    def pacificAtlantic(self, heights: [[int]]) -> [[int]]:
        def dfs(q):
            ret = set()

            while q:
                pop_item = q.pop()
                r, c = pop_item[0], pop_item[1]
                # 記可以流入海洋的點
                ret.add((r, c))

                # 往四個方向走
                # 向上
                # (tmp_r, tmp_c) in ret -> 防重複, heights[tmp_r][tmp_c] < heights[r][c] -> 阻擋流入海洋的條件
                tmp_r, tmp_c = r - 1, c
                if tmp_r < 0 or tmp_r >= rows or tmp_c < 0 or tmp_c >= cols or (tmp_r, tmp_c) in ret or heights[tmp_r][tmp_c] < heights[r][c]:
                    pass
                else:
                    ret.add((tmp_r, tmp_c))
                    q.append((tmp_r, tmp_c))

                # 向下
                tmp_r, tmp_c = r + 1, c
                if tmp_r < 0 or tmp_r >= rows or tmp_c < 0 or tmp_c >= cols or (tmp_r, tmp_c) in ret or heights[tmp_r][tmp_c] < heights[r][c]:
                    pass
                else:
                    ret.add((tmp_r, tmp_c))
                    q.append((tmp_r, tmp_c))

                # 向左
                tmp_r, tmp_c = r, c - 1
                if tmp_r < 0 or tmp_r >= rows or tmp_c < 0 or tmp_c >= cols or (tmp_r, tmp_c) in ret or heights[tmp_r][tmp_c] < heights[r][c]:
                    pass
                else:
                    ret.add((tmp_r, tmp_c))
                    q.append((tmp_r, tmp_c))

                # 向右
                tmp_r, tmp_c = r, c + 1
                if tmp_r < 0 or tmp_r >= rows or tmp_c < 0 or tmp_c >= cols or (tmp_r, tmp_c) in ret or heights[tmp_r][tmp_c] < heights[r][c]:
                    pass
                else:
                    ret.add((tmp_r, tmp_c))
                    q.append((tmp_r, tmp_c))

            return ret

        rows = len(heights)
        cols = len(heights[0])

        # 處理pacific
        pacific_list = []
        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    pacific_list.append((row, col))
        pacific_set = dfs(pacific_list)
        pacific_result = list(pacific_set)

        # 處理atlantic
        atlantic_list = []
        for row in range(rows):
            for col in range(cols):
                if row == rows - 1 or col == cols - 1:
                    atlantic_list.append((row, col))
        atlantic_set = dfs(atlantic_list)
        atlantic_result = list(atlantic_set)

        result = []
        # 取交集
        for item in pacific_result:
            if item in atlantic_result:
                result.append(item)

        return result

    def pacificAtlantic_2(self, heights: [[int]]) -> [[int]]:
        def dfs(q, result):
            while q:
                pop_item = q.pop()
                result.add(pop_item)

                r = pop_item[0]
                c = pop_item[1]
                # 這個pop_item需要跟上下左右來比高度
                # 上
                if (r - 1) < 0 or (r - 1) >= rows or c < 0 or c >= cols or (r - 1, c) in result or heights[r][c] > heights[r - 1][c]:
                    pass
                else:
                    # 找到了
                    # 要加入result
                    result.add((r - 1, c))
                    # 要在加到q裡面，再去向此位置的4個方位比較
                    q.append((r - 1, c))

                # 下
                if (r + 1) < 0 or (r + 1) >= rows or c < 0 or c >= cols or (r + 1, c) in result or heights[r][c] > heights[r + 1][c]:
                    pass
                else:
                    result.add((r + 1, c))
                    q.append((r + 1, c))

                # 左
                if r < 0 or r >= rows or (c - 1) < 0 or (c - 1) >= cols or (r, c - 1) in result or heights[r][c] > heights[r][c - 1]:
                    pass
                else:
                    result.add((r, c - 1))
                    q.append((r, c - 1))

                # 右
                if r < 0 or r >= rows or (c + 1) < 0 or (c + 1) >= cols or (r, c + 1) in result or heights[r][c] > heights[r][c + 1]:
                    pass
                else:
                    result.add((r, c + 1))
                    q.append((r, c + 1))

        rows = len(heights)
        cols = len(heights[0])
        # 處理pacific
        pacific_list = []
        pacific_result_list = set()
        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    pacific_list.append((row, col))
        dfs(pacific_list, pacific_result_list)
        print(pacific_result_list)

        # 處理Atlantic
        atlantic_list = []
        atlantic_result_list = set()
        for row in range(rows):
            for col in range(cols):
                if row == (rows - 1) or col == (cols - 1):
                    atlantic_list.append((row, col))
        dfs(atlantic_list, atlantic_result_list)

        # 取交集
        result = []
        for item in pacific_result_list:
            if item in atlantic_result_list:
                result.append(list(item))

        print(result)
        return result


if __name__ == '__main__':
    solution = Solution()
    solution.pacificAtlantic_2(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])