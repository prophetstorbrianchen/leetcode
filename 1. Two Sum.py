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


if __name__ == '__main__':
    solution = Solution()
    solution.twoSum(nums = [3,3], target = 6)