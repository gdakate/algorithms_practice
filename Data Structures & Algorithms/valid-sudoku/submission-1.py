class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        col = [set() for _ in range(9)]
        row = [set() for _ in range(9)]
        box =[set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v==".":
                    continue
                boxes = (i//3)*3+(j//3)
                if v in col[i] or v in row[j] or v in box[boxes]:
                    return False 
                col[i].add(v)
                row[j].add(v)
                box[boxes].add(v)

        return True