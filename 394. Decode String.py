class Solution:
    # hint
    # 使用stack，然後使用倒敘的方式
    # https://www.youtube.com/watch?v=qB0zZpBJlh8
    def decodeString(self, s: str) -> str:
        stack = []

        # 先把所有的數字英文括號放入stack
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                # 處理字串的部分
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr

                # 把"["給pop掉
                stack.pop()

                # 處理數字的部分
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                # 防"2[abc]xyz[cd]ef" -> 但題目號好像有說左括號前必定要為integer
                if k == "":
                    k = 1
                # 必須要再把組合好的substr放入stack中
                stack.append(int(k) * substr)

        res = "".join(stack)
        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.decodeString(s = "2[abc]0[cd]ef")