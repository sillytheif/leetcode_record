class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        count = 0
        i = 0
        while i<len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i = i+1
        return len(nums)