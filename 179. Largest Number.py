from functools import cmp_to_key


class Solution:
    # hint
    # 需要使用python的tool來排 key=cmp_to_key(compare)
    # [30, 34] -> 3034 vs 3430 -> 3034 < 3430 ->[34, 30]
    # https://www.youtube.com/watch?v=WDx6Y4i4xJ8
    def largestNumber(self, nums: [int]) -> str:
        def compare(a, b):
            if int(str(a) + str(b)) > int(str(b) + str(a)):
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare), reverse=False)

        # **edge case**
        """
        if [0] * len(nums) == nums:
            print("0")
            return "0"
        """

        res = ""
        for n in nums:
            res = res + str(n)

        # 使用這個方法就可以不加edge case
        # [0, 0] -> "00" -> int("00") -> 0
        print(str(int(res)))
        return str(int(res))

    def largestNumber_2(self, nums: [int]) -> str:
        def fun(a, b):
            # [30, 34] -> 3034 vs 3430 -> 3034 < 3430 ->[34, 30]
            if int(str(a) + str(b)) > int(str(b) + str(a)):
                return -1
            else:
                return 1

        # **這個函式(cmp_to_key)非常容易忘記 -> 可以自訂交換的公式**
        nums = sorted(nums, key=cmp_to_key(fun), reverse=False)

        nums_string = ""
        for n in nums:
            nums_string = nums_string + str(n)

        # **防止"00"這種string -> int("00")為0 => 先轉int，去除00**
        return str(int(nums_string))


if __name__ == '__main__':
    solution = Solution()
    solution.largestNumber_2(nums = [0,0])