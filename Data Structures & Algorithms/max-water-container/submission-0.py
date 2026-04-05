# 노가다 : 인덱스 차이 * 둘중 min 너비 최대. 왼쪽 움직이는 버전, 오른쪽 움직이는버전.. 
# 자료구조 : 투포인터. max에 저장

# 높이 짧은쪽을 이동시키는 방향으로. 

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left =0 
        right = len(heights)-1
        max = 0
        while left<right:
            h = min(heights[left], heights[right])
            w = right-left
            size = h*w
            if size>max : max = size
            if heights[left]<heights[right]:
                left +=1
            else:
                right-=1
            
            
        return max