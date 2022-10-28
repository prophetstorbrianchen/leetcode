class Solution:
    # hint
    # 這題跟我的想法差很多，需要學習
    # 自己要畫一次圖
    # https://leetcode.cn/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode-solution/
    def longestValidParentheses(self, s: str) -> int:
        # method 之前的想法 -> 可以算出合法總數，但無法解掉何時能夠reset res的解
        """
        # 使用stack
        stack = []
        res = 0
        longest = 0

        # 當stack為空，進來的為")" -> 直接不進stack
        for i, c in enumerate(s):
            # 一開始為")"即為不合法
            if not stack and c == ")":
                continue

            if not stack and c == "(":
                stack.append(c)
                continue

            # 如果碰到合法的直接result + 2，直接pop
            if stack[-1] == "(" and c == ")":
                stack.pop()
                res = res + 2
                longest = max(longest, res)
            elif stack[-1] == "(":
                stack.append(c)
            else:
                # 碰到不合法，直接reset stack和res
                res = 0
                stack = []

        print(longest)
        return longest
        """

        # method 2 -> 使用stack去記index
        max_lenght = 0
        # 這是一個技巧
        stack = [-1]

        # stack是存index
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                # 碰到")" -> pop掉
                stack.pop()

                # 但如果stack是空的時候，仍要放入")" -> 這需要想一下，因為是使用index來計算
                if not stack:
                    stack.append(i)
                else:
                    # 使用index的差值，去得到當前的最大括號數
                    max_lenght = max(max_lenght, i - stack[-1])

        print(max_lenght)
        return max_lenght


if __name__ == '__main__':
    solution = Solution()
    solution.longestValidParentheses(s = "(()())")