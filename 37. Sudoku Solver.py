import collections


class Solution:
    # hint
    # 不知道怎麼設backtracking
    # 不太懂回傳true/false的這種dfs或是backtracking
    # https://leetcode.cn/problems/sudoku-solver/solution/37-jie-shu-du-hui-su-sou-suo-suan-fa-xiang-jie-by-/
    # https://leetcode.cn/problems/sudoku-solver/solution/pythonsethui-su-chao-guo-95-by-mai-mai-mai-mai-zi/
    # https://leetcode.com/problems/sudoku-solver/discuss/866333/Python%3A-Backtracking-%2B-HashMapsSets-%2B-Complexity-%2B-Explanation -> 這個方法向N皇后那堤，可以try看看
    # https://blog.csdn.net/L141210113/article/details/88419719
    def __init__(self):
        self.row_table = collections.defaultdict(set)
        self.col_table = collections.defaultdict(set)
        # key為tuple -> (r/3, c/3); dict的key不能為list,但可以為tuple
        self.square_table = collections.defaultdict(set)
        self.empty = []

    def isValidSudoku(self, board: [[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                # 把結果記錄在這3個table裡面
                if board[r][c] == ".":
                    self.empty.append((r, c))
                    continue
                else:
                    if board[r][c] not in self.row_table[r] and board[r][c] not in self.col_table[c] and board[r][c] not in self.square_table[(int(r / 3), int(c / 3))]:
                        self.row_table[r].add(board[r][c])
                        self.col_table[c].add(board[r][c])
                        self.square_table[(int(r / 3), int(c / 3))].add(board[r][c])
                        # 因為是要商數，這樣做也行
                        # square_table[(r // 3), (c // 3))].add(board[r][c])
                    else:
                        print(False)
                        return False
        print(True)
        return True

    def solveSudoku(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # method 1 -> 只用正向的方式，紀錄所有未走過的位置，以及不可用的數字
        self.isValidSudoku(board)

        def dfs(iter):
            # 把空的都補完了
            # base case
            if iter == len(self.empty):  # 处理完empty代表找到了答案
                return True

            # 解析出空的空格位置
            r, c = self.empty[iter]

            for val in '123456789':
                if val in self.row_table[r] or val in self.col_table[c] or val in self.square_table[(int(r / 3), int(c / 3))]:
                    continue

                # place:
                board[r][c] = val
                self.row_table[r].add(val)
                self.col_table[c].add(val)
                self.square_table[(int(r / 3), int(c / 3))].add(val)

                # next:
                # 如果為True，就返回
                # 如果為False，就返回上一層，並remove掉之前寫得直
                # 使用bool的dfs就是這種用法 -> 藥習慣
                if dfs(iter + 1):
                    return True

                # remove:
                # 退回上層
                board[r][c] = "."
                self.row_table[r].remove(val)
                self.col_table[c].remove(val)
                self.square_table[(int(r / 3), int(c / 3))].remove(val)
            return False

        dfs(0)
        print(board)


        """
        # method 2 -> 只用反向的方式，紀錄所有未走過的位置，以及可用的數字
        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字

        empty = []  # 收集需填数位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':  # 更新可用数字
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3) * 3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        def backtrack(iter=0):
            if iter == len(empty):  # 处理完empty代表找到了答案
                return True
            i, j = empty[iter]
            b = (i // 3) * 3 + j // 3
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(iter + 1):
                    return True
                row[i].add(val)  # 回溯
                col[j].add(val)
                block[b].add(val)
            return False

        backtrack()
        """

        """
        # method 3 -> 容易理解，但不知道True和False的意思
        def isValid(x, y):
            tmp = board[x][y];
            board[x][y] = 'D'
            for i in range(9):
                if board[i][y] == tmp: return False
            for i in range(9):
                if board[x][i] == tmp: return False
            for i in range(3):
                for j in range(3):
                    if board[int(x / 3) * 3 + i][int(y / 3) * 3 + j] == tmp: return False
            board[x][y] = tmp
            return True

        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in '123456789':
                            board[i][j] = k
                            print(isValid(i, j))
                            if isValid(i, j) and dfs(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True

        dfs(board)
        print(board)
        """



if __name__ == '__main__':
    solution = Solution()
    solution.solveSudoku(board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])