import collections


class Solution:
    def validNum(self, n: int) -> [int]:
        # https://www.hjwu.me/posts/interview_quiz2/
        # backtracking
        self.number = n

        count_dict = collections.defaultdict(int)
        for n in str(self.number):
            count_dict[n] = count_dict[n] + 1

        # print(count_dict)

        def dfs(res):
            if len(res) == len(str(self.number)):
                if res not in result:
                    result.append(res)

            for n in str(self.number):
                if count_dict[n] == 0:
                    continue
                else:
                    # 準備進下一層
                    count_dict[n] = count_dict[n] - 1
                    # 進下一層
                    dfs(res + n)
                    # 回上一層
                    count_dict[n] = count_dict[n] + 1

        result = []
        dfs("")
        print(result)
        # process valid num
        count = 0
        for n in result:
            if len(str(int(n))) == len(str(self.number)):
                count = count + 1
        print(count)


if __name__ == '__main__':
    solution = Solution()
    solution.validNum(n = 1234)