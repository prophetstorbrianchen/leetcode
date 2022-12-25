import collections


class Solution:
    # hint
    # 模仿爬山完就是要下山
    # 一剛開始就是下山或是平的 -> 直接往下一個走
    # 找到peak
    # 找到peak後，若是平的或是向上爬 -> 直接往下一個走
    # 找到peak後，若是向下走
    # 找到山 -> 算山的寬度
    def longestMountain(self, arr: [int]) -> int:
        i = ans = 0
        while i < len(arr):
            # base和peak很重要
            base = i
            # walk up
            while i + 1 < len(arr) and arr[i] < arr[i + 1]:
                i = i + 1

            # check if peak is valid
            # 把一剛開始是下坡或平的的情況就直接排除
            if i == base:
                i = i + 1
                continue

            # 找到peak
            peak = i

            # walk down
            while i + 1 < len(arr) and arr[i] > arr[i + 1]:
                i = i + 1

            # check if end is valid
            # 只要後半部是平的就不是山 -> 特別重要
            if i == peak:
                i = i + 1
                continue

            # update answer
            ans = max(ans, i - base + 1)

        # print(ans)
        return ans


if __name__ == '__main__':
    solution = Solution()
    solution.longestMountain(arr = [2,1,4,7,3,2,5])