class Solution(object):
    def majorityElement(self, nums):
        hash_table_dict = {}
        for item in nums:
            if item not in hash_table_dict:
                hash_table_dict[item] = 1
            else:
                hash_table_dict[item] = hash_table_dict[item] + 1

        # 同時找出key的最大值以及key
        max_val = max(hash_table_dict, key=hash_table_dict.get)
        return max_val

    def majorityElement_2(self, nums):
        num = ""
        digital = float("-inf")
        sorted_num = sorted(nums)
        sorted_num.append("a")
        count = 0
        for i in range(len(sorted_num) - 1):
            if sorted_num[i + 1] == sorted_num[i]:
                count = count + 1
                if count >= digital:
                    num = sorted_num[i]
                    digital = count
            else:
                count = 0
                if count >= digital:
                    num = sorted_num[i]
                    digital = count
        # print(num, digital)
        return num


if __name__ == '__main__':
    solution = Solution()
    solution.majorityElement(nums = [3,2,3])
    solution.majorityElement_2(nums=[1])
