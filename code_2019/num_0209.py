class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        temp_sum = 0
        ans = 0
        left = 0
        for i in range(n):
            temp_sum +=nums[i]
            while temp_sum>=s:
                temp_sum -