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

    def longestValidParentheses_2(self, s: str) -> int:
        # 使用stack來記括號的index
        # 初始stack要先給-1 -> 為了好算(可以自己推一下)
        # 碰到"(" -> append; 碰到")" -> pop
        # **但有一情況例外 -> "())" 連續2個")" -> 此時的stack已經是不合法的了，所以直接填上第二個")"的index在stack裡面(可以理解成重新reset，前面的那些都不算數了)**
        # 正常狀況下，可以去得到當前的合法括號數目

        stack = [-1]
        max_valid_length = 0
        for i, par in enumerate(s):
            if par == "(":
                stack.append(i)
            else:
                stack.pop()

                # 例外狀況，若是不放裡面，也會造成stack為空，使的下次stack.pop code error
                if not stack:
                    stack.append(i)
                else:
                    max_valid_length = max(max_valid_length, i - stack[-1])

        return max_valid_length


if __name__ == '__main__':
    solution = Solution()
    solution.longestValidParentheses(s = "(()())")