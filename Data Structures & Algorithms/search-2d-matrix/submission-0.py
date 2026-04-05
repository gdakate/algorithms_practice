# 2차원 배열의 바이너리.. 각 행별 중간값과 비교?
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target<matrix[0][0] or target>matrix[len(matrix)-1][len(matrix[0])-1]:
            return False
        
        for i in range(len(matrix)):
            left = 0
            right = len(matrix[0])-1

            if target<=matrix[i][right]:
                while left<=right:
                    mid = (left+right)//2
                    if target>matrix[i][mid]:
                        left = mid+1
                    elif target == matrix[i][mid]: 
                        return True
                    else :
                        right = mid-1
        
        return False
            