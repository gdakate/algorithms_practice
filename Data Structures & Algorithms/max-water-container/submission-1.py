class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        
        max_area = 0
        while left<right :
            h = min(heights[right],heights[left])
            w = right -left
            area = h*w
            if area >max_area :
                max_area = area
            if heights[right]<heights[left]:
                right -=1
            else :
                left +=1
            max_area= max(area,max_area)
        return max_area
                
