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


if __name__ == '__main__':
    solution = Solution()
    solution.threeSum(nums = [3,0,-2,-1,1,2])