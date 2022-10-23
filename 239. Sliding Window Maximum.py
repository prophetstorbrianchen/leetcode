from collections import deque


class Solution:
    # hint
    # 使用雙頭queue的方式
    # 當進來的數筆queue的最後一筆小，就pop queue中的數，不然就push
    # 當q_index[0]出了滑動窗口的範圍，就是要被pop出去
    # https://maxming0.github.io/2020/11/28/Sliding-Window-Maximum/
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        n = len(nums)
        res = []
        q_index = deque()

        # q_index是紀錄位置
        # i是跑到list的index
        for i in range(n):
            # 當進來的數筆queue的最後一筆小，就pop queue中的數
            while q_index and nums[q_index[-1]] < nums[i]:
                q_index.pop()

            # 不然就一直放進去
            q_index.append(i)

            # 當q_index[0]出了滑動窗口的範圍，就是要被pop出去
            # 可以想一下[7,2,4] k=2的例子，7在第二次時就要因為位置不再滑動窗口的位置內而被pop
            # **不能用長度去看，因為前面有機會一直pop，所以並非滿queue的狀態 -> 不能使用len(q_index) > k**
            if q_index[0] == i - k:
                q_index.popleft()

            # 如果k=3時，前2個數是不列入計算的 -> 要從[2]開始才能算
            # 因為每次的最大值都keep在最左邊，所以就是取q[0]
            if i >= k - 1:
                res.append(nums[q_index[0]])

        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.maxSlidingWindow(nums = [7,2,4], k = 2)