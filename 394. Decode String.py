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

    def decodeString_2(self, s: str) -> str:
        # 從正序去loop，有碰到右括號時的先處理，然後放入stack -> "3[a]2[bc]" -> 先處理3a存入stack -> [aaa, bcbc]
        # 碰到巢狀時，就會自動從後面往前處理 -> "3[a2[c]]" -> 3[acc] -> [accaccacc]
        # 使用倒敘的方式loop回來
        # 碰到右括號直接pop
        # 結算到左括號前的string -> 看左括號前面數字是多少就loop幾次
        # 算完再放回去

        stack = []
        # 重點在於用從頭開始loop，我自己寫的時候，只有解到巢狀結構是正確的而已
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                # 到著來
                string = ""
                while stack[-1] != "[":
                    tmp_c = stack.pop()
                    # **這樣就reverser了**
                    string = tmp_c + string

                # 碰到左括號 -> 把左括號pop掉
                stack.pop()

                # **碰到數字 -> 處理數字, 這真的很神要學**
                k = ""
                while stack and stack[-1].isdigit():
                    # **這樣就正序了**
                    k = stack.pop() + k

                # 乘回去，放入stack
                tmp_string = ""
                for _ in range(int(k)):
                    tmp_string = tmp_string + string
                stack.append(tmp_string)
                # stack.append(int(k) * string)

        print(str(stack))
        res = "".join(stack)
        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.decodeString_2(s = "100[leetcode]")