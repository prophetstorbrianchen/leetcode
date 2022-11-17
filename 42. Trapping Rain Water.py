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

    def trap_2(self, height: [int]) -> int:
        # 使用雙指標
        # 需要4個變數: left, right, maxleft, maxright
        # left每次往右走，如果比當前的maxleft大 -> 就會更新maxleft
        # right每次往左走，如果比當前的maxright大 -> 就會更新maxright
        # 如果left比目前的maxleft小 -> 算左半部面積
        # 如果right比目前的maxright小 -> 算右半部面積
        # 更新left和right的位置 -> 若是height[left] > height[right] -> right 向左移動，反之向右移動(看你要判斷哪邊，另一邊就是else而已)

        # index
        left = 0
        right = len(height) - 1

        # 高度
        maxleft = 0
        maxright = 0

        left_area = 0
        right_area = 0
        while left < right:
            # 每次更新最大值
            maxleft = max(height[left], maxleft)
            maxright = max(height[right], maxright)

            # 判斷左右指針向左向右
            # **不要把高度和index混著用(誤用)需要很清楚各自代表的意思**
            # **要先算完面積，才能移動指針**
            if height[left] < height[right]:
                left_area = left_area + (maxleft - height[left])
                left = left + 1
            else:
                right_area = right_area + (maxright - height[right])
                right = right - 1

        total_area = left_area + right_area
        print(total_area)
        return total_area


if __name__ == '__main__':
    solution = Solution()
    solution.trap_2(height = [0,1,0,2,1,0,1,3,2,1,2,1])