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


if __name__ == '__main__':
    solution = Solution()
    # solution.threeSum(nums = [3,0,-2,-1,1,2])
    solution.threeSum_2(nums = [2,0,-2,-5,-5,-3,2,-4])