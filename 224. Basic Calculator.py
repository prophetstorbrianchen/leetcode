class Solution:
    # 重點在於-(a+b)這種的處理 -> 無論括號裡面做啥事情，出來都要*(-1)
    # 有括號時才需要疊ops
    # 如果括號有負數時，那ops要疊負-1
    # https://leetcode.cn/problems/basic-calculator/solution/ji-ben-ji-suan-qi-by-leetcode-solution-jvir/
    # example: 1+2+(3-(4+5))
    # 1+2 时，由于当前位置没有被任何括号所包含，则栈顶元素为初始值 +1+1；
    # 1+2+(3 时，当前位置被一个括号所包含，该括号前面的符号为 ++ 号，因此栈顶元素依然 +1+1；
    # 1+2+(3-(4 时，当前位置被两个括号所包含，分别对应着 ++ 号和 -− 号，由于 ++ 号和 -− 号合并的结果为 -− 号，因此栈顶元素变为 -1−1。
    def calculate(self, s: str) -> int:
        ops = [1]
        sign = 1

        ret = 0
        n = len(s)
        i = 0
        while i < n:
            # 空白無意義 -> 只有位置往下走
            if s[i] == ' ':
                i += 1
            # sign是為了解決+和-號
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            # 仔細想1-(2+3)這種case -> 是1-2-3而非1-2+3
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                # 為這種case
                # "123456"
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                ret += num * sign

        print(ret)
        return ret


if __name__ == '__main__':
    solution = Solution()
    solution.calculate(s = "(3-(4+5))")
    # solution.calculate(s="4-5")
    # solution.calculate(s="2147483647") -> num = num * 10 + ord(s[i]) - ord('0')