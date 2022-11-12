class Solution:
    # hint
    # 使用index來控制digits的位置->可達到上下層的效果
    # 串成dfs的方式很厲害
    # https://www.youtube.com/watch?v=0snEunUacZY
    def letterCombinations(self, digits: str) -> [str]:
        res = []
        res = []
        digitsToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "pqrs",
            "7": "tuv",
            "8": "wxyz",
        }

        def dfs(i, curStr):
            # base case
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            # digits="23 -? digits[0] -> 2 ; digits[1] -> 3 => 即可控制上下層的關係
            # i 是控制digits的位數
            # 很神的寫法
            for c in digitsToChar[digits[i]]:
                dfs(i + 1, curStr + c)

        # index = 0，必定從0開始去算第一位
        if digits:
            dfs(0, "")

        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.letterCombinations(digits = "25")