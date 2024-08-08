class Solution:
    def __init__(self):
        self.quadMapping = {
            "00": 1,
            "01": 2,
            "02": 3,
            "10": 4,
            "11": 5,
            "12": 6,
            "20": 7,
            "21": 8,
            "22": 9
        }

    def isValidSudoku(self, board):
        rows = {}
        cols = {}
        quads = {}

        for rowIndex in range(9):
            for colIndex in range(9):
                quadIndex = self.getQuadrant(rowIndex, colIndex)
                cell = board[rowIndex][colIndex]
                if cell != ".":
                    
                    # Check row
                    if rowIndex not in rows:
                        rows[rowIndex] = set()
                    if cell in rows[rowIndex]:
                        return False
                    rows[rowIndex].add(cell)

                    # Check column
                    if colIndex not in cols:
                        cols[colIndex] = set()
                    if cell in cols[colIndex]:
                        return False
                    cols[colIndex].add(cell)

                    # Check quadrant
                    if quadIndex not in quads:
                        quads[quadIndex] = set()
                    if cell in quads[quadIndex]:
                        return False
                    quads[quadIndex].add(cell)

        return True
    
    def getQuadrant(self, row, col):
        horizontal = str(row // 3)
        vertical = str(col // 3)

        return self.quadMapping[horizontal + vertical]

if __name__ == "__main__":
    solution = Solution()
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(solution.isValidSudoku(board))