class Solution:
    def asteroidCollision(self, asteroids: [int]) -> [int]:
        # method 1 -> 寫得不太好，很醜的解法
        stack = []
        for item in asteroids:
            if not stack:
                stack.append(item)
                continue

            temp = 100
            while temp != 0:
                if not stack:
                    stack.append(item)
                    break

                if (item > 0 and stack[-1] > 0) or (item < 0 and stack[-1] < 0) or (stack[-1] < 0 and item > 0):
                    # 同向/負在左正在右
                    stack.append(item)
                    temp = 0
                else:
                    # 相向
                    # 開始比，看誰大，放入stack
                    if abs(stack[-1]) > abs(item):
                        temp = 0
                    elif abs(stack[-1]) < abs(item):
                        temp = stack.pop()
                    elif abs(stack[-1]) == abs(item):
                        if stack[-1] == item:
                            # [-2 ] -2
                            stack.append(item)
                            temp = 0
                        else:
                            # [2] -2
                            stack.pop()
                            break
        print(stack)
        return stack


if __name__ == '__main__':
    solution = Solution()
    solution.asteroidCollision(asteroids = [8,-8])
