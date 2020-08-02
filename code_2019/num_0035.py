class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]>=target:
                return i

        return len(nums)

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0]>=target:
            return 0
        head = 0
        end = len(nums) -1
        while head<=end:
            mid = (head+end)>>1
            if nums[mid]==target or (nums[mid]>target and nums[mid-1]<target):
                return mid
            elif nums[mid]>target:
                end = mid -1
            else:
                head = head +1