class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_index = 0
        right_index = len(height)-1
        max_area =[]
        while left_index < right_index:
            temp = (right_index-left_index)*min(height[left_index],height[right_index])
            max_area.append(temp)
            if height[left_index]<height[right_index]:
                left_index = left_index+1
            else:
                right_index = right_index-1
        answer = max(max_area)
        return answer