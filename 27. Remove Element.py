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


if __name__ == '__main__':
    solution = Solution()
    solution.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)