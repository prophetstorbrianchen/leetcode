class Solution:
    # hint
    # sort和雙指針
    # 如何跳過重複的數字
    def threeSum(self, nums: [int]) -> [[int]]:
        sorted_nums = sorted(nums)
        res = []

        for i, n in enumerate(sorted_nums):
            if i > 0 and sorted_nums[i - 1] == n:
                continue
            two_sum = 0 - n

            l = i + 1
            r = len(sorted_nums) - 1
            while l < r:
                # 這段看筆記，就會很明白
                if sorted_nums[l] + sorted_nums[r] < two_sum:
                    l = l + 1
                elif sorted_nums[l] + sorted_nums[r] > two_sum:
                    r = r - 1
                else:
                    # 找到two sum，仍要進下一個位數，那這邊就是統一用l來向右移動
                    res.append([n, sorted_nums[l], sorted_nums[r]])
                    l = l + 1
                    # 檢查看有沒有走到重覆的
                    while sorted_nums[l] == sorted_nums[l - 1] and l < r:
                        l = l + 1
        print(res)
        return res

    def threeSum_2(self, nums: [int]) -> [[int]]:
        # sort
        sorted_nums = sorted(nums)

        res = []
        for i, n in enumerate(sorted_nums):
            # **防超出邊界的方法**
            # **如果後面一個和前面一個一樣，就跳過 -> 去重的方法**
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            two_sum = 0 - n

            seen = {}
            # **
            for j, a in enumerate(sorted_nums[i + 1:]):
                b = two_sum - a

                if b not in seen:
                    seen[a] = j
                else:
                    # find two sum
                    temp_list = [a, b]

                    # find three sum
                    temp_list.append(n)

                    # ****prevent [0,0,0,0] -> [[0,0,0], [0,0,0]]****
                    if temp_list in res:
                        pass
                    else:
                        res.append(temp_list)

        print(res)
        return res

    def threeSum_hash_table(self, nums: [int]) -> [[int]]:
        # 使用hash table
        nums.sort()
        result = []
        for i, n in enumerate(nums):
            two_sum = 0 - n
            seen = {}
            for j in range(i + 1, len(nums)):
                # b為nums[j]所需要的值 -> 記載hash table中 -> 若是下一次的nums[j]剛好為b表示找到了
                b = two_sum - nums[j]

                # 如果需要nums[j]的值沒有在seen裡面 -> 把b值和j的index存起來
                if nums[j] not in seen:
                    seen[b] = j
                else:
                    res = [nums[j], b]
                    res.insert(0, n)

                    if res not in result:
                        result.append(res)

        # print(result)
        return result

    def threeSum_two_pointer(self, nums: [int]) -> [[int]]:
        # use two pointer
        nums.sort()

        result = []
        for i, n in enumerate(nums):
            # **去重 -> 要使用後面比前面的方式來做，注意要是 i > 0 **
            if i > 0 and nums[i - 1] == n:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                if (n + nums[l] + nums[r]) < 0:
                    l = l + 1
                elif (n + nums[l] + nums[r]) > 0:
                    r = r - 1
                else:
                    # find
                    """
                    if [n, nums[l], nums[r]] in result:
                        pass
                    else:
                        result.append([n, nums[l], nums[r]])
                    """
                    result.append([n, nums[l], nums[r]])
                    l = l + 1
                    # **這邊很重要，容易忘記 -> 去除重複的**
                    while l < r and nums[l] == nums[l - 1]:
                        l = l + 1

        # print(result)
        return result


if __name__ == '__main__':
    solution = Solution()
    solution.threeSum_two_pointer(nums = [0,0,0])
    # solution.threeSum_hash_table(nums = [2,0,-2,-5,-5,-3,2,-4])