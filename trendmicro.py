import collections
from collections import Counter


class Solution:
    # robert和我的考題
    def question_1(self, S):
        occurrences = [0] * 26
        for i in range(len(S)):
            occurrences[ord(S[i]) - ord('a')] += 1
        best_char = 'a'
        best_res = 0
        for i in range(1, 26):
            if occurrences[i] >= best_res:
                best_char = chr(ord('a') + i)
                best_res = occurrences[i]
        best_index = occurrences.index(best_res)
        best_char = chr(ord('a') + best_index)
        print(best_res, best_char)
        return best_res

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

    """
    # 無法使用self的解法
    def solution(B):
        # Implement your solution here
        # use dfs to find shape
        def dfs(r, c, arr):
            if r < 0 or r >= len(metric) or c < 0 or c >= len(metric[0]) or metric[r][c] == ".":
                return
            
            metric[r][c] = "."
            arr[0] = arr[0] + 1
    
            # top
            dfs(r - 1, c, arr)
    
            # down
            dfs(r + 1, c, arr)
    
            # left
            dfs(r, c - 1, arr)
    
            # right
            dfs(r, c + 1, arr)
    
    
        metric = []
        # transfer string to list
        for item in B:
            tmp = []
            for s in item:
                tmp.append(s)
            metric.append(tmp)
    
        rows = len(metric)
        cols = len(metric[0])
    
        res = [0,0,0]
        a = [0]
        for row in range(rows):
            for col in range(cols):
                if metric[row][col] == ".":
                    continue
                else:
                    a[0] = 0
                    dfs(row, col, a)
    
                    if a[0] == 3:
                        res[2] = res[2] + 1
                    elif a[0] == 2:
                        res[1] = res[1] + 1
                    elif a[0] == 1:
                        res[0] = res[0] + 1
                    else:
                        pass
                    
        return res
    """


class Solution_2:
    # 學姊的考題
    def question_1(self, A, B):
        result = 0
        # 先找出最大值
        max_possible_length = int((A + B) / 4)

        # 在從最大值往下遞減，直到對A和對B可以做出最大的value，且可以做出正方形
        for i in range(max_possible_length, -1, -1):
            if i > 0:
                num_side = int(A / i) + int(B / i)
                if num_side >= 4:
                    return i

    def question_2(self, A):
        # 在同一列只能算一次
        new_a = []
        for row_item in A:
            new_a.append(list(set(row_item)))

        hash_table = collections.defaultdict(int)

        for list_item in new_a:
            for item in list_item:
                hash_table[item] = hash_table[item] + 1

        count = 0
        for id, value in hash_table.items():
            if value >= 2:
                count = count + 1

        # print(count)
        return count

    def question_3(self, S):
        # hint
        # 這題學姊的方法不太對
        def check_odd(data):
            odd_list = []
            for c, f in Counter(data).items():
                if f % 2 == 1:
                    odd_list.append(c)
            return odd_list

        freq = Counter(S)
        output = {}
        for start in range(len(S)):
            s = S[start]
            if freq[s] > 1:
                data = S[start:]
                odd_list = check_odd(data)
                if len(odd_list) == 1:
                    last = data.index(odd_list[0])
                    output[data[:last]] = len(data[:last])
                if not odd_list:
                    output[data] = len(data)

        print(max(output.values()))
        return max(output.values())

        # method2
        """
        freq = Counter(S)
        max_length = 0
        print(freq)
        output = {}
        left = 0
        for left in range(len(S)):
            if freq[S[left]] > 1:
                data = S[left:..]
                odd_list = check_odds(data)
                if odd_list:
                    for right in range(len(S)-1, 1, -1):
                        data = S[left:right]
                        odd_list = check_odds(data)
                        if not odd_list and data:
                            output[data] = len(data)
                else:
                    output[data] = len(data)
        if output:
            max_length = max(output.values())
        return max_length
        """

    def question_4(self, s):
        # Stores the total
        # count of substrings

        n = len(s)
        count = 0

        # Traverse the range [0, N]:
        for i in range(n):

            # Traverse the range [i + 1, N]
            for j in range(i + 1, n + 1):
                # Stores the substring over
                # the range of indices [i, len]
                test_str = (s[i: j])
                print(test_str)

                # Stores the frequency of characters
                res = {}

                # Count frequency of each character
                for keys in test_str:
                    res[keys] = res.get(keys, 0) + 1

                flag = 0
                # Traverse the dictionary
                for keys in res:
                    # If any of the keys
                    # have odd count
                    if res[keys] % 2 != 0:
                        flag = 1
                        break

                # Otherwise
                if flag == 0:
                    # print(test_str)
                    count += 1

        # Return count
        print(count)
        return count


if __name__ == '__main__':
    solution = Solution()
    # array = [1,3,6,1,6,6,9,9]
    # array = [5,1,4,3]
    # array = [2,2,2,3,2,3]
    # solution.question_2(array=array)

    # B = ["##.","#.#",".##"]
    # B = [".#..#", "##..#", "...#."]
    # B = [".##.#", "#.#..", "#...#", "#.##."]
    # B = ["...", "...", "..."]
    # solution.question_3(arr=B)

    solution2 = Solution_2()
    # A = [[1,2,2],[3,1,4]]
    # A = [[1,1,5,2,3], [4,5,6,4,3],[9,4,4,1,5]]
    # A = [[4,3],[5,5],[6,2]]
    # solution2.question_1(A=A)
    S = "zthtzh"
    solution2.question_4(s=S)
