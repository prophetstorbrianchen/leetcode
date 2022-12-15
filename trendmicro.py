import collections


class Solution:
    def question_2(self, array: list):
        # method 1 - only hashtable
        """
        hash_dict = collections.defaultdict(int)

        max_value = -1
        for i, n in enumerate(array):
            if n not in hash_dict:
                hash_dict[n] = i
            else:
                start_index = hash_dict[n]
                end_index = i + 1
                max_value = max(max_value, sum(array[start_index: end_index]))

        # print(max_value)
        return max_value
        """

        # method 2 - prefixsum and hashtable
        hash_dict = collections.defaultdict(int)
        prefix_sum = []

        # build prefixsum_list
        sum = 0
        prefix_sum.append(0)
        for n in array:
            sum = sum + n
            prefix_sum.append(sum)

        # build hash table and get the max_value
        max_value = -1
        for i, n in enumerate(array):
            if n not in hash_dict:
                hash_dict[n] = i
            else:
                # prefixsum_list 和 array的位置差一格
                # [0,2,4,6,9,11,14], {2:0, 3:3}
                start_sum = prefix_sum[hash_dict[n]]
                end_sum = prefix_sum[i + 1]
                max_value = max(max_value, end_sum - start_sum)

        print(max_value)
        return max_value

    def question_3(self, arr: list):
        # dfs - 不使用回傳直
        def dfs(r, c):
            # base case
            if r < 0 or r >= len(self.metric) or c < 0 or c >= len(self.metric[0]) or self.metric[r][c] == ".":
                return

            self.metric[r][c] = "."
            self.i = self.i + 1

            # 上
            dfs(r - 1, c)

            # 下
            dfs(r + 1, c)

            # 左
            dfs(r, c - 1)

            # 右
            dfs(r, c + 1)

        # string 轉 list
        self.metric = []
        for item in arr:
            tmp = []
            for s in item:
                tmp.append(s)
            self.metric.append(tmp)

        rows = len(self.metric)
        cols = len(self.metric[0])

        res = [0,0,0]
        for row in range(rows):
            for col in range(cols):
                if self.metric[row][col] == ".":
                    continue
                else:
                    # 每次self.i都重記
                    self.i = 0
                    dfs(row, col)
                    # print(value)

                    if self.i == 3:
                        res[2] = res[2] + 1
                    elif self.i == 2:
                        res[1] = res[1] + 1
                    elif self.i == 1:
                        res[0] = res[0] + 1
                    else:
                        pass

        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    array = [1,3,6,1,6,6,9,9]
    # array = [5,1,4,3]
    # array = [2,2,2,3,2,3]
    # solution.question_2(array=array)

    # B = ["##.","#.#",".##"]
    # B = [".#..#", "##..#", "...#."]
    # B = [".##.#", "#.#..", "#...#", "#.##."]
    B = ["...", "...", "..."]
    solution.question_3(arr=B)