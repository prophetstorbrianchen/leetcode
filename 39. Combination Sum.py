class Solution:
    # hint
    # 這題是backtracking的基礎題，必要熟練
    # 把剩餘的值和所經過的路徑帶入下層的方式
    # 這題是用DFS紀錄走過路徑的方式
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        """
        def dfs(cur, path):
            # base case
            if cur == 0:
                res.append(path)
                return

            # 每個都要輪過
            for n in candidates:
                # 用base case去想
                if n > cur:
                    return

                # 不重複的方法，這個蠻重要的
                if path and n < path[-1]:
                    continue

                # 進下一層
                # 把剩餘的值和所經過的路徑帶入下層
                dfs(cur - n, path + [n])


        res = []
        candidates.sort()
        dfs(target, [])
        print(res)
        return res
        """

        def dfs(cur, path, depth):
            # base case
            if cur == 0:
                res.append(path)
                return

            # 每個都要輪過
            for n in candidates:
                # 用base case去想
                if n > cur:
                    return

                # 不重複的方法，這個蠻重要的
                if path and n < path[-1]:
                    continue

                # 進下一層
                # 把剩餘的值和所經過的路徑帶入下層

                # 這樣做cur永遠到不了7，run過第一輪時只會到5，因為在第一層是cur=5 -> cur = 7-2
                # 所以dfs在處理數字時，通常是帶入參數時再順便給進去
                """
                cur = cur - n
                path = path + [n]
                depth = depth + 1
                print(depth, cur, path)
                dfs(cur, path, depth)
                """

                print(depth + 1, cur - n, path + [n])
                dfs(cur - n, path + [n], depth + 1)
        res = []
        candidates.sort()
        dfs(target, [], 0)
        print(res)
        return res

    def combinationSum_2(self, candidates: [int], target: int) -> [[int]]:
        def dfs(cur, path):
            # base case
            # 當扣到小於0，回上層
            if cur < 0:
                return

            # 當扣到等於0，找到解
            if cur == 0:
                res.append(path)

            for n in candidates:
                # 不重複的方法，這個蠻重要的
                if path and n < path[-1]:
                    continue

                # **為什麼不能這樣帶 -> 因為會改到當層cur的值 -> 假設本層cur=7但cur = cur - 2 -> cur就變成5
                # 所以你可以設個變數去assign，這樣就不會改到當層cur
                # 在遞迴的式子中盡量不要assign回自己，這樣原本的值會被蓋掉
                """
                if cur - n >= 0:
                    cur = cur - n
                    path = path + [n]
                    dfs(cur, path)
                """
                # 可改成這樣
                """
                f cur - n >= 0:
                    next_cur = cur - n
                    next_path = path + [n]
                    dfs(next_cur, next_path)
                """
                """
                path.append(n)
                """

                if cur - n >= 0:
                    dfs(cur - n, path + [n])

        # 先做sort
        res = []
        candidates.sort()

        # **運用[]，隨著每層去增減，這是技巧，但也是我的問題**
        dfs(target, [])
        print(res)


if __name__ == '__main__':
    solution = Solution()
    # solution.combinationSum(candidates = [2,3,6,7], target = 7)
    solution.combinationSum_2(candidates=[2, 3, 6, 7], target=7)