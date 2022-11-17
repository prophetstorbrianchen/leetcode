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

    def dailyTemperatures_2(self, temperatures: [int]) -> [int]:
        # 要有一個stack來存天數，因為沒有超過是給0，有超過才看天數 -> 預設給0的list(省去很多麻煩)
        # 每次均放入一個溫度 -> for loop
        # 新的溫度要去對留下來的溫度比 -> 如果新的溫度比舊的溫度高pop，直到裡面為空或者是裡面舊的溫度比新的溫度高就停 -> while loop
        # pop出來的就可以得知天數
        # 畫一次就知道了 -> 這個模板是經典模板使用for去loop所有的num，使用while去做stack的pop

        temperatures_stack = []
        res_stack = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            while temperatures_stack and temperatures_stack[-1][1] < temperature:
                tmp_index, tmp_temperature = temperatures_stack.pop()
                res_stack[tmp_index] = i - tmp_index

            temperatures_stack.append((i, temperature))

        print(res_stack)
        return res_stack


if __name__ == '__main__':
    solution = Solution()
    solution.dailyTemperatures_2(temperatures = [73,74,75,71,69,72,76,73])