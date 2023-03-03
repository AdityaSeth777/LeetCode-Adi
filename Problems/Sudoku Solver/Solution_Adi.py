class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(x: int, y: int, c: str) -> bool:
            for i in range(9):
                if board[i][y] == c:
                    return False
                if board[x][i] == c:
                    return False
                if board[3 * (x // 3) + i // 3][3 * (y // 3) + i % 3] == c:
                    return False
            return True

        def solveHelper() -> bool:
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for c in '123456789':
                            if isValid(i, j, c):
                                board[i][j] = c
                                if solveHelper():
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        solveHelper()