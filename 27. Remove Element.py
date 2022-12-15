from functools import cmp_to_key


class Solution:
    # 第一種方法比較乾淨俐落，但比較投機一點，因為用了-1來替代
    # 第二種方法，就是用移的方式去處理
    def removeElement(self, nums: [int], val: int) -> int:
        # method 1
        # 先使用-1來取代，之後再sort
        count = 0
        for i, n in enumerate(nums):
            if n == val:
                nums[i] = -1
                continue
            else:
                count = count + 1

        nums.sort(reverse=True)
        return count

        # method 2
        # 先sort完，再用後面得數取代前面
        """
        nums.sort()
        
        # edge case
        if len(nums) == 0:
            return 0

        if val not in nums:
            return len(nums)
        else:
            index_list = []
            for i, n in enumerate(nums):
                if n == val:
                    index_list.append(i)
    
            end_index = index_list[-1]
            count = len(index_list)
    
            for i in range(len(nums)):
                if i > end_index:
                    nums[i - count] = nums[i]
    
            return len(nums) - count
        """

    def removeElement_2(self, nums: [int], val: int) -> int:
        # 先做sort -> 這種sort，是內部的swap，並非assign一個新值
        nums.sort()

        # val沒有在nums的情況
        if val not in nums:
            return len(nums)

        # 紀錄val的index，之後要換位置
        val_index_list = []
        val_count = 0
        for i, n in enumerate(nums):
            if n == val:
                val_count = val_count + 1
                val_index_list.append(i)

        # 位置交換 -> 2要被後面的3和4assign就好，也不需要交換(因為只檢查前面)
        # [0,0,1,2,2,2,3,4] -> [0,0,1,3,4,2,3,4]
        for i in range(len(nums)):
            # 這是推出來的公式，可以自己畫一次
            if i >= (val_index_list[-1] + 1):
                nums[i - val_count] = nums[i]

        print(nums)
        return len(nums) - val_count

    def removeElement_3(self, nums: [int], val: int) -> int:
        # 這樣沒有in place
        def fun(a, b):
            if b == val:
                return -1
            else:
                return 0

        val_count = 0
        for i, n in enumerate(nums):
            if n == val:
                val_count = val_count + 1

        nums.sort(key=cmp_to_key(fun), reverse=False)
        print(nums)
        return val_count


if __name__ == '__main__':
    solution = Solution()
    solution.removeElement_3(nums = [0,1,2,2,3,0,4,2], val = 2)