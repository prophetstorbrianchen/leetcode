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




if __name__ == '__main__':
    solution = Solution()
    solution.generateParenthesis(n = 3)