import copy


class Solution:
    # hint
    # 當open < n 時，只增加open
    # close < open時，只增加close
    # open = close = n -> 合法
    # https://www.youtube.com/watch?v=s9fokUqJ76A
    # 之後可以用[] + ")" 來替代append
    # 把"("想成左子樹，把")"想成左子樹 -> 一直向左下找，沒找到就回上層往右子樹找
    def generateParenthesis(self, n: int) -> [str]:
        stack = []
        res = []

        def dfs(openN, closeN):
            # base case
            if openN == closeN == n:
                res.append("".join(stack))

            # 想成左子數
            if openN < n:
                stack.append("(")
                # 進下一層
                dfs(openN + 1, closeN)
                # 回上一層要pop掉
                stack.pop()

            # 想成左子數
            if closeN < openN:
                stack.append(")")
                dfs(openN, closeN + 1)
                stack.pop()

        dfs(0, 0)
        print(res)
        return res

    def generateParenthesis_2(self, n: int) -> [str]:
        # 往下長的規則與順序
        # 當左括號小於n時，要增加左括號
        # 當右括號小於左括號時，要增加右括號
        # 左右括號數最後必定相等
        # 把左括想成左子樹
        # 把右括想成右子樹
        # backtracking

        def dfs(l, r, res):
            # base case
            # 左右括號數最後必定相等 -> 表示找到我們要的
            if l == r == n:
                tmp_result.append(copy.deepcopy(res))
                return

            # 當左括號小於n時，要增加左括號 -> l < n
            if l < n:
                # 準備進下一層
                dfs(l + 1, r, res + ["("])

            # 當右括號小於左括號時，要增加右括號 -> l < n
            if r < l:
                dfs(l, r + 1, res + [")"])

        tmp_result = []
        dfs(0, 0, [])

        result = []
        # process to string
        for item in tmp_result:
            result.append("".join(item))

        return result


if __name__ == '__main__':
    solution = Solution()
    solution.generateParenthesis(n = 3)