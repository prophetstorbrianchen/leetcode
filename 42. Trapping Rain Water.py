class Solution:
    # hint
    # 使用雙指針
    # 要設定l, r, l_max, r_max -> 此題關鍵
    # 可以看動畫
    # https://leetcode.cn/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode-solution-tuvc/
    def trap(self, height: [int]) -> int:
        # 訂出雙指針以及left_max, right_max
        l, r = 0, len(height) - 1

        # l_max, r_max會依照l和r所走過得而更新
        l_max, r_max = 0, 0

        # 積水部分
        res = 0

        # 左右指針相向走
        # 左半部-> 使用l_max和height[l]求出積水的部分
        # 右半部-> 使用r_max和height[r]求出積水的部分
        while l < r:
            # 每次更新l_max和height[l]之間的高度差來求
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            if height[l] < height[r]:
                # l向右移
                res = res + (l_max - height[l])
                l = l + 1
            else:
                # r向左移
                res = res + (r_max - height[r])
                r = r - 1

        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])