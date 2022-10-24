class Solution:
    # 畫一次就知道
    # 加号：将数字压入栈；
    # 减号：将数字的相反数压入栈；
    # 乘除号：计算数字与栈顶元素，并将栈顶元素替换为计算结果。
    # https://leetcode.cn/problems/basic-calculator-ii/solution/ji-ben-ji-suan-qi-ii-by-leetcode-solutio-cm28/
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []

        # 对于第一个数字，其之前的运算符视为加号 -> 這個很重要，會決定後面的num是要放入stack還是要先pop處理完再放進去
        preSign = '+'
        num = 0

        for i in range(n):
            # 慣用的方法要記
            if s[i] != ' ' and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if i == n - 1 or s[i] in '+-*/':
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(num * -1)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                # 這部分是最重要的，後面的num都會看preSign來決定動作
                preSign = s[i]
                num = 0
        return sum(stack)


if __name__ == '__main__':
    solution = Solution()
    solution.calculate(s = "3+2*2")
