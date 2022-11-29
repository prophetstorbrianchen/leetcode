class Solution:
    # hint
    # 這題沒看過解答很難解得出來 -> 常人會使用hash table去做
    # 此題不能使用hash table
    # 使用insertIndex紀錄每次不相等i-1和i -> assign nums[i] 給 nums[insertIndex] -> 找到不相等insertIndex就要加1(記住下一個應該填不一樣位置的index)
    # 這有點難理解，需要多記幾次
    def removeDuplicates(self, nums: [int]) -> int:
        # method 1
        """
        insertIndex = 1
        for i in range(1, len(nums)):
            # 如果一樣，就不需要特別紀錄insertIndex -> 不一樣才要記錄
            # 當然他只換前面幾個而已，後面就不理他了
            if nums[i - 1] != nums[i]:
                nums[insertIndex] = nums[i]
                insertIndex = insertIndex + 1

        print(nums, insertIndex)
        return insertIndex
        """

        # method 2
        # 使用list的insert/del/pop/append
        # 每次刪掉都要重算一次 -> 因為del or pop之後，index不回空著
        # 每次一減(nums的個數)一加(i) -> 最後一定會平衡
        # i != len(nums) - 1 -> [0,1,1,2,2,3] -> [0,1,2,2,3] -> [0,1,2,3]
        i = 0
        while i != len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i]
            else:
                # 不相等時i就要+1
                i += 1

        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    solution.removeDuplicates(nums = [1,1,2])