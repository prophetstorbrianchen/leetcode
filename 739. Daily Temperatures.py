class Solution:
    # hint
    # 可以自己畫一次，沒有很難
    # https://leetcode.cn/problems/daily-temperatures/solution/mei-ri-wen-du-by-leetcode-solution/
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        length = len(temperatures)
        ans = [0] * length
        # stack是存index
        stack = []
        for i in range(length):
            # 當前溫度
            temperature = temperatures[i]

            # 當stack不為空而且當前溫度 > stack的最上面的溫度時 -> 就要pop top的那個，並利用index的差來算出天數
            while stack and temperature > temperatures[stack[-1]]:
                # pop
                prev_index = stack.pop()
                # 算天數
                ans[prev_index] = i - prev_index

            # 該pop掉的都pop掉了，就可以將最新的那個index向上疊
            stack.append(i)
        return ans


if __name__ == '__main__':
    solution = Solution()
    solution.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])