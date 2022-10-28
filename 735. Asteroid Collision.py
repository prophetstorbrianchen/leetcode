class Solution:
    def asteroidCollision(self, asteroids: [int]) -> [int]:
        # method 1 -> 寫得不太好，很醜的解法
        stack = []
        for item in asteroids:
            if not stack:
                stack.append(item)
                continue

            notCollession = False
            while notCollession is False:
                if not stack:
                    stack.append(item)
                    break

                if (item > 0 and stack[-1] > 0) or (item < 0 and stack[-1] < 0) or (stack[-1] < 0 and item > 0):
                    # 同向/負在左正在右
                    stack.append(item)
                    notCollession = True
                else:
                    # 相向
                    # 開始比，看誰大，放入stack
                    if abs(stack[-1]) > abs(item):
                        notCollession = True
                    elif abs(stack[-1]) < abs(item):
                        stack.pop()
                        notCollession = False
                    elif abs(stack[-1]) == abs(item):
                        if stack[-1] == item:
                            # [-2 ] -2
                            stack.append(item)
                            notCollession = True
                        else:
                            # [2] -2
                            stack.pop()
                            break
        print(stack)
        return stack


if __name__ == '__main__':
    solution = Solution()
    solution.asteroidCollision(asteroids = [-2,-1,1,-2])
