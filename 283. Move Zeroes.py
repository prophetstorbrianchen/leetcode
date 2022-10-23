from functools import cmp_to_key


class Solution:
    # hint
    # 注意sorted和sort
    # nums = sorted(nums) -> 等於是複製在assign的sort，這並非in-place instead
    # nums.sort -> 這才是in-place的sort
    # 第一種方法是自訂compare的方式，然後做交換
    # 第二種方法是用雙指針
    def moveZeroes(self, nums: [int]) -> None:
        def compare(a, b):
            if b == 0:
                return -1
            else:
                return 1

        nums.sort(key=cmp_to_key(compare), reverse=False)
        print(nums)


if __name__ == '__main__':
    solution = Solution()
    solution.moveZeroes(nums = [0,1,0,3,12])