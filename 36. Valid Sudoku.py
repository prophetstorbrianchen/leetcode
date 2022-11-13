import collections


class Solution:
    # hint
    # 要比對的這種，基本上都要用到hash table
    # 做3張表
    # https://www.youtube.com/watch?v=TjFXEUCMqI8
    def isValidSudoku(self, board: [[str]]) -> bool:
        # method 1
        """
        rows = len(board)
        cols = len(board[0])

        row_table = collections.defaultdict(set)
        col_table = collections.defaultdict(set)
        # key為tuple -> (r/3, c/3); dict的key不能為list,但可以為tuple
        square_table = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                row_table[r] = set()
                row_table[c] = set()
                square_table[(int(r/3), int(c/3))] = set()

        for r in range(rows):
            for c in range(cols):
                # 把結果記錄在這3個table裡面
                if board[r][c] == ".":
                    continue
                else:
                    if board[r][c] not in row_table[r] and board[r][c] not in col_table[c] and board[r][c] not in square_table[(int(r/3), int(c/3))]:
                        row_table[r].add(board[r][c])
                        col_table[c].add(board[r][c])
                        square_table[(int(r/3), int(c/3))].add(board[r][c])
                    else:
                        print(False)
                        return False
        print(True)
        return True
        """

        # method 2 -> 在dict的地方改進 -> 其實因為已經是collections.defaultdict(set)的作法，所以不需要再重建一個表
        # board[r][c] not in row_table[r] -> 直接這樣給沒有問題，這就是collections.defaultdict(set)的好處
        rows = len(board)
        cols = len(board[0])

        row_table = collections.defaultdict(set)
        col_table = collections.defaultdict(set)
        # key為tuple -> (r/3, c/3); dict的key不能為list,但可以為tuple
        square_table = collections.defaultdict(set)

        for r in range(rows):
            for c in range(cols):
                # 把結果記錄在這3個table裡面
                if board[r][c] == ".":
                    continue
                else:
                    if board[r][c] not in row_table[r] and board[r][c] not in col_table[c] and board[r][c] not in square_table[(int(r / 3), int(c / 3))]:
                        row_table[r].add(board[r][c])
                        col_table[c].add(board[r][c])
                        square_table[(int(r / 3), int(c / 3))].add(board[r][c])
                        # 因為是要商數，這樣做也行
                        # square_table[(r // 3), (c // 3))].add(board[r][c])
                    else:
                        print(False)
                        return False
        print(True)
        return True


if __name__ == '__main__':
    solution = Solution()
    solution.isValidSudoku(board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])