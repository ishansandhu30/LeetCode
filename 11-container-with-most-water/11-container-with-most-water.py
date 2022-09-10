class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        n=length-1
        left = 0
        right = len(height)-1
        area = 0
        while left<=right: 
            if height[left]<height[right]:
                area = max(area, height[left]*n)
                left+=1
                n-=1
            else:
                area = max(area, height[right]*n)
                right-=1
                n-=1
            
        return area
        
                