class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        if size<=2:
            return 0
        import numpy as np
        max_left = np.zeros([size],dtype = int)
        max_righ = np.zeros([size],dtype = int)
        max_left[0] = height[0]
        max_righ[size-1] = height[size-1]
        for i in range(1,size):
            max_left[i] = max(max_left[i-1],height[i])
            max_righ[size-1-i] = max(max_righ[size-i],height[size-1-i])
        answer = 0
        for i in range(1,size-1):
            answer+= min(max_righ[i],max_left[i]) - height[i]
        return answer

a = Solution()
print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))