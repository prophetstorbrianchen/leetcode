class Solution:
    # 使用部分和去做
    # 一步一步算出和，然後和記錄在dict中
    # 若和減K之後有在dict找到時，res就加1
    # 看筆記，這題多看幾次
    # 小名得比較好懂
    # https://maxming0.github.io/2020/04/26/Subarray-Sum-Equals-K/
    def subarraySum(self, nums: [int], k: int) -> int:
        dic = {}

        # 這個是prefix常見的作法，nums = [4], k = 4時，就可以解釋
        dic[0] = 1
        res = 0

        s = 0
        for n in nums:
            s = s + n

            # 檢查需要的值有沒有在dic中
            if s - k in dic:
                res = res + dic[s - k]

            if s not in dic:
                dic[s] = 0

            # 每一次都要記錄
            dic[s] = dic[s] + 1

        return res

    def subarraySum_2(self, nums: [int], k: int) -> int:
        # 使用prefix和hashtable來做
        hash_table = {0: 1}

        prefix_sum = 0
        res = 0
        for n in nums:
            prefix_sum = prefix_sum + n

            # 要注意是+hash_table[prefix_sum - k]而非+1 -> 沒有很懂
            if prefix_sum - k in hash_table:
                res = res + hash_table[prefix_sum - k]

            if prefix_sum not in hash_table:
                hash_table[prefix_sum] = 0
            hash_table[prefix_sum] = hash_table[prefix_sum] + 1

        return res


if __name__ == '__main__':
    solution = Solution()
    solution.subarraySum(nums = [1,2,3], k = 3)