class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      row = [set() for _ in range(9)]
      col = [set() for _ in range(9)]
      boxes = [set() for _ in range(9)]

      for r in range (9):
            for c in range(9):
                v = board[r][c]
                if v == '.':
                    continue
                box = (r//3)*3+(c//3) # 좌표 체크
                if v in row[r] or v in col[c] or v in boxes[box]: #중복체크
                    return False
                row[r].add(v) 
                col[c].add(v)
                boxes[box].add(v)
      return True
