from collections import deque
# 雙端佇列
# append(): 新增元素於佇列右側
# appendleft(): 新增元素於佇列左側
# pop(): 刪除最右側元素
# popleft(): 刪除最左側元素


class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        while k > 0:
            tmp = nums.pop()
            nums.insert(0, tmp)
            k = k - 1

        print(nums)


if __name__ == '__main__':
    solution = Solution()
    solution.rotate(nums = [1,2,3], k = 4)
