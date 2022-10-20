class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # valid operators
        operators = ["+", "-", "*", "/"]

        # set stack
        stack = []

        for t in tokens:
            if t in operators:
                number1 = int(stack.pop())
                number2 = int(stack.pop())

                if t == "+":
                    result = number2 + number1
                elif t == "-":
                    result = number2 - number1
                elif t == "*":
                    result = number2 * number1
                else:
                    result = number2 / number1

                # result = exec("number2 t number1")
                stack.append(result)
            else:
                stack.append(t)

        print(int(stack[0]))
        return int(stack[0])


if __name__ == '__main__':
    solution = Solution()
    solution.evalRPN(tokens = ["2","1","+","3","*"])