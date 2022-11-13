import collections


class Solution:
    # hint
    # 不知道怎麼設backtracking
    # https://leetcode.com/problems/sudoku-solver/discuss/866333/Python%3A-Backtracking-%2B-HashMapsSets-%2B-Complexity-%2B-Explanation -> 這個方法向N皇后那堤，可以try看看
    # https://blog.csdn.net/L141210113/article/details/88419719
    def __init__(self):
        self.row_table = collections.defaultdict(set)
        self.col_table = collections.defaultdict(set)
        # key為tuple -> (r/3, c/3); dict的key不能為list,但可以為tuple
        self.square_table = collections.defaultdict(set)

    def isValidSudoku(self, board: [[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                # 把結果記錄在這3個table裡面
                if board[r][c] == ".":
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
        """
        res = []
        self.isValidSudoku(board)
        def dfs(i, board):
            if i == 8:
                return
            
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for val in '123456789':
                            if val in self.row_table[r] or val in self.col_table[c] or val in self.square_table[(int(r / 3), int(c / 3))]:
                                continue

                            # place:
                            board[r][c] = val
                            self.row_table[r].add(val)
                            self.col_table[c].add(val)
                            self.square_table[(int(r / 3), int(c / 3))].add(val)

                            # next:
                            dfs(i + 1, board)

                            # remove:
                            board[r][c] = "."
                            self.row_table[r].remove(val)
                            self.col_table[c].remove(val)
                            self.square_table[(int(r / 3), int(c / 3))].remove(val)

        dfs(0, board)
        print(board)
        """

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



if __name__ == '__main__':
    solution = Solution()
    solution.solveSudoku(board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])