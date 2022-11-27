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

    def letterCombinations_2(self, digits: str) -> [str]:
        # 最後字串的結果長度必須要和digits一樣
        # 建立數字和字母的hash table
        # 排列組合類的backtracking
        hash_table = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def dfs(i, res):
            # 最後字串的結果長度必須要和digits一樣 -> 找到答案
            if len(res) == len(digits):
                result.append(res)
                return

            # 這太神了，我只能模仿
            for c in hash_table[digits[i]]:
                dfs(i + 1, res + c)

        result = []
        # edge case -> digits = ""
        if digits:
            dfs(0, "")
        return result


if __name__ == '__main__':
    solution = Solution()
    solution.letterCombinations_2(digits = "23")