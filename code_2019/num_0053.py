class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N =len(nums)
        if N==1:
            return nums[0]
        max_end_ssubArrat = [nums[0]]
        for i in range(1,N):
            temp = max_end_ssubArrat[-1]
            if temp>0:
                max_end_ssubArrat.append(temp+nums[i])
            else:
                max_end_ssubArrat.append(nums[i])
        return max(max_end_ssubArrat)
a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))