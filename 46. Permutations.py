class Solution:
    # hint
    # 我使用combination sum的方式去做，當然也可參考其他解法
    # https://blog.csdn.net/fuxuemingzhu/article/details/79363903
    # neetcode的就不是很好懂
    # https://www.youtube.com/watch?v=s7AvT7cGdSo
    def permute(self, nums: [int]) -> [[int]]:
        # dfs
        def dfs(p):
            # 有找到
            if len(p) == len(nums):
                res.append(p)
                return

            # 往下層走
            for n in nums:
                if n not in visit:
                    next_p = p + [n]
                    # 同一條path避免重複
                    visit.add(n)
                    dfs(next_p)
                    # 回上層之後要拿掉
                    visit.remove(n)

        res = []
        visit = set()
        dfs([])
        print(res)
        return res

    def permute_2(self, nums: [int]) -> [[int]]:
        # list要滿才是答案 -> P3取1 -> 3! -> 3*2*1
        # list中的順序可以不固定

        def dfs(res):
            if len(res) == len(nums):
                result.append(res)

            for n in nums:
                # 重複，找下一個數
                if n in res:
                    continue
                else:
                    # 進下一層
                    dfs(res + [n])

        result = []
        dfs([])
        # print(result)
        return result


if __name__ == '__main__':
    solution = Solution()
    solution.permute(nums = [1,2,3])