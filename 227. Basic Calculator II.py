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

    def calculate_2(self, s: str) -> int:
        # 此題的重點就是把運算後的結果全部放入stack裡面 -> sum(stack)即是結果
        # **一開始必須要先給一個preSign = '+'，不然格數一定會錯**
        # **必須知道sting如何轉數字，這有點技巧在裡面. "1" -> 1, "12" -> 10+2, "123" -> 100+20+3
        # 正數 + -> push n
        # 碰到 - -> push n * (-1)
        # 碰到 * -> pop之後*完，在push進去
        # 碰到 * -> pop之後/完，在push進去

        # "3+2*2" -> 第一次是3就變成+3放入
        preSign = "+"
        stack = []
        num = 0
        for i in range(len(s)):
            # string轉數字
            if s[i] != " " and s[i].isdigit():
                # 記住這個技巧str轉int時 -> print(ord('1') - ord('0')) -> 1
                num = num * 10 + ord(s[i]) - ord('0')
            # **這個的意思 i == len(s) - 1 -> 保障最後一個數也是能夠被加減乘除的**
            if i == len(s) - 1 or s[i] in '+-*/':
                # 使用上一次的加減乘除號
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(num * (-1))
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))

                # 記著這一次的加減乘除號
                # 每個加減乘除號之後都是一個新的數
                preSign = s[i]
                num = 0

        print(sum(stack))
        return sum(stack)


if __name__ == '__main__':
    print(ord('1') - ord('0'))
    solution = Solution()
    solution.calculate_2(s = "3+2*2")
