class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxed = [[set() for _ in range(3)] for _ in range(3)]
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    if val in rows[r]:
                        return(False)
                    rows[r].add(val)
                    if val in cols[c]:
                        return(False)
                    cols[c].add(val)
                    if val in boxed[r//3][c//3]:
                        return(False)
                    boxed[r//3][c//3].add(val)
        return True