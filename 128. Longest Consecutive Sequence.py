class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        # 先做set先把重複的去除
        nums = set(nums)

        # 對數列作排序，即可得知有沒有連續數
        sorted_nums = sorted(list(nums))
        # print(sorted_nums)

        # 這是為了不要超過list的index小撇步，讓code變得更簡單，不需要做額外處理
        # 如果不加這行，在pointer + 1時就會超出邊界
        sorted_nums.append(float('inf'))

        longest_length = 0
        count = 1
        pointer = 0
        while pointer < len(sorted_nums) - 1:
            # 定義連續和不連續
            if sorted_nums[pointer] + 1 == sorted_nums[pointer + 1]:
                count = count + 1
                longest_length = max(longest_length, count)
            else:
                count = 1
                longest_length = max(longest_length, count)

            # 往右走一格
            pointer = pointer + 1
        print(longest_length)
        return longest_length

    def longestConsecutive_2(self, nums: [int]) -> int:
        # 排序 去重
        sorted_nums = sorted(set(nums))

        # 比較好做
        sorted_nums.append(float("inf"))

        pointer = 0
        max_length = 0
        # **注意count是要從1開始計算**
        count = 1
        while pointer < len(sorted_nums) - 1:
            # 連續時count +1
            if sorted_nums[pointer] + 1 == sorted_nums[pointer + 1]:
                count = count + 1
            else:
                # 不連續時count重算
                max_length = max(max_length, count)
                count = 1

            pointer = pointer + 1

        print(max_length)
        return max_length



if __name__ == '__main__':
    solution = Solution()
    solution.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1])
    solution.longestConsecutive_2(nums = [100,4,200,1,3,2])
