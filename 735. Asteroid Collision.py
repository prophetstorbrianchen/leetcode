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

    def asteroidCollision_2(self, asteroids: [int]) -> [int]:
        ans = []
        for new in asteroids:
            # 我思路是對的，但在while中判斷是錯的 -> 相向時在會撞
            # 原來可以while else的作法
            # 比完再pop就好，不需要先pop
            # 會無限loop的stack題目，比較少見，這是其中一題
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    # 這個continue很重要，可以一直比較
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                # **注意這個break，停止while loop的重點 -> 在不合這些規定時就break掉 -> 新進的element沒有辦法造成相撞時，就表示這個stack已經穩定**
                break
            else:
                ans.append(new)
        print(ans)
        return ans


if __name__ == '__main__':
    solution = Solution()
    solution.asteroidCollision_2(asteroids = [5,10,-5])
