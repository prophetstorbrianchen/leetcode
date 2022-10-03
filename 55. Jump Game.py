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


if __name__ == '__main__':
    solution = Solution()
    solution.canJump(nums = [2,3,1,1,4])