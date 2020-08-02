class Solution:
    def search(self, nums, target):
 
        if not nums:
            return -1
        return self.binarySearch(nums, target, 0, len(nums)-1)

    def binarySearch(self, nums, target, start, end):
        if end < start:
            return -1
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        if nums[start] <= target < nums[mid]: # left side is sorted and has target
            return self.binarySearch(nums, target, start, mid-1)
        elif nums[mid] < target <= nums[end]: # right side is sorted and has target
            return self.binarySearch(nums, target, mid+1, end)
        elif nums[mid] > nums[end]: # right side is pivoted
            return self.binarySearch(nums, target, mid+1, end)
        else: # left side is pivoted
            return self.binarySearch(nums, target, start, mid-1)


class Solution2():
    def search(self,nums,target):
        if len(nums)==0:
            return -1
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target<=nums[right]:
                left = mid+1
            elif nums[left]<=target<nums[mid]:
                right = mid-1
            elif nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid -1
        if nums[left]==target:
            return left
        else:
            return -1
a =Solution2()
print(a.search([4,5,6,7,0,1,2],0))