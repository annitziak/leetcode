class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0 
        right , left = 0 , len(height)-1
        while right<left:
            width = left-right
            heights = min(height[right],height[left])
            max_area = max(max_area, width * heights)
            if height[right]>=height[left]:
                left-=1
            else:
                right+=1
        return max_area