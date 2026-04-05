# 2차원 배열의 바이너리.. 각 행별 중간값과 비교?
# 1차원으로 펼쳐놓고 보기
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        left = 0
        right = row*col -1

        while left<=right:
            mid = (left+right)//2

            r = mid//col 
            c = mid%col # 나머지
            value = matrix[r][c]

            if value<target:
                left = mid +1
            elif value == target:
                return True
            else :
                right = mid-1

        return False
