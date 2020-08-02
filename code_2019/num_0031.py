class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        flag = 0
        length = len(nums)
        #import pdb;pdb.set_trace()
        if length==1 or length==0:
            return
        for i in range(1,len(nums)):
            if nums[length-i]>nums[length-i-1]:
                head = length - i
                end = length -1
                while head<end:
                    temp = nums[head]
                    nums[head] = nums[end]
                    nums[end] = temp
                    head =head+1
                    end = end -1
                insert_mask = nums[length-i-1]
                j = length-i

                while insert_mask>=nums[j]:
                    j = j+1
                nums[length-i-1] = nums[j]
                nums[j] = insert_mask
                flag =1
                break
        if flag == 1:
            return nums
        else:
            head = 0
            end = length-1
            while head < end:
                temp = nums[head]
                nums[head] = nums[end]
                nums[end] = temp
                head = head + 1
                end = end - 1
            return nums


nums = [1,5,1]
a =Solution()

print(a.nextPermutation(nums))