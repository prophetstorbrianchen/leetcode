class Solution:
    # hint
    # 看影片和筆記
    # https://maxming0.github.io/2020/04/26/Jump-Game/
    def canJump(self, nums: [int]) -> bool:
        reach = 0

        for cur, num in enumerate(nums):
            if reach < cur:
                return False

            # 以reach能跳到最遠當reach，每次更新reach
            reach = max(reach, cur + num)
        return True

    # **正常情況R動的要跟C一樣甚至要比C還快 -> [1,1,1,1] or [2,3,1,1,4]**
    # **edge case: 當某些點碰到0時，R會比C還慢 -> [0, 2, 3] or [3,2,1,0,4] -> 這就是R比C還慢，這種狀況怎麼跑都不會到**
    def canJump_2(self, nums: [int]) -> bool:
        r = 0
        for c, n in enumerate(nums):
            # **這是edge case，要熟記**
            if r < c:
                return False

            r = max(r, c + n)

        print(True)
        return True


if __name__ == '__main__':
    solution = Solution()
    solution.canJump_2(nums = [1, 1])