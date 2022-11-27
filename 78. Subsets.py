import copy

class Solution:
    # hint
    # 我是憑感覺寫出code的，實際上我的是反向解法，跟我note裡化的不太一樣
    def subsets(self, nums: [int]) -> [[int]]:
        # dfs
        def dfs(p):
            res.append(p)

            # 往下層走
            for n in nums:
                # 如果沒有在p的list中，就往下層走
                if n not in p:
                    next_p = p + [n]
                    # 同一條path避免重複
                    dfs(next_p)
                else:
                    # 有在p中就回上層
                    return

        res = []
        dfs([])
        print(res)
        return res

    def subsets_2(self, nums: [int]) -> [[int]]:
        # 不能有重複地往下走

        def dfs(res):
            result.append(copy.deepcopy(res))

            for n in nums:
                # 不重複才能向下走
                if n not in res:
                    # 進入下一層
                    res.append(n)
                    dfs(res)
                    res.pop()
                else:
                    # 重複了，回上層
                    return

        result = []
        dfs([])
        return result


if __name__ == '__main__':
    solution = Solution()
    solution.subsets_2(nums=[1, 2, 3])