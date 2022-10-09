class Solution:
    # 這題還是很不熟
    # 重點在a + b = target -> a = target - b
    # 但是hash table的建法必須是list中的值和index
    def twoSum(self, nums: [int], target: int) -> [int]:
        seen = {}
        for i, b in enumerate(nums):
            # core logic:  a + b = target -> a = target - b
            a = target - b
            # use hashtables to implement lookups as they are extremely fast
            if a not in seen:
                seen[b] = i
            else:
                print([seen[a], i])
                return [seen[a], i]

    def twoSum_2(self, nums: [int], target: int) -> [int]:
        # hash table
        seen = {}

        for i, n in enumerate(nums):
            a = target - n
            if a not in seen:
                seen[n] = i
            else:
                print([seen[a], i])
                return [seen[a], i]


if __name__ == '__main__':
    solution = Solution()
    solution.twoSum(nums = [2,7,11,15], target = 9)
    solution.twoSum_2(nums = [3,2,4], target = 6)