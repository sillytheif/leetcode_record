class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_index = 0
        i = 0
        N = len(nums)-1
        if N == 0:
            return True
        while min_index<N:
            if i==min_index and nums[i]==0:
                return False
            if i+nums[i]<=min_index:
                i = i+1
                continue
            min_index = nums[i]+i
            i = i+1
        return True

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        i = length-2
        while(i>=0):
            if nums[i]<length-1-i:
                i-=1
            else:
                length=i+1
                i=length-2
        if length ==1:
            return True
        else:
            return False

a =Solution()
print(a.canJump([3,2,1,0,4]))