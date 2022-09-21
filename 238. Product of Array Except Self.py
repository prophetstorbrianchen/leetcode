class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        res = []

        # 建立prefix
        prefix_init = 1
        prefix_list = [1]
        for i in range(len(nums)):
            prefix_init = prefix_init * nums[i]
            prefix_list.append(prefix_init)
        #print(prefix_list)

        # 建立postfix
        postfix_init = 1
        postfix_list = [1]
        for i in range(len(nums) -1, -1, -1):
            postfix_init = postfix_init * nums[i]
            postfix_list.append(postfix_init)
        #postfix_list.reverse()
        #print(postfix_list[::-1])
        postfix_list_reverse = postfix_list[::-1]

        for index in range(len(nums)):
            res.append(prefix_list[index] * postfix_list_reverse[index + 1])

        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.productExceptSelf(nums = [1,2,3,4])