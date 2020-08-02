class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        answer=[]
        if len(nums)<=3:
            return []
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                head = j+1
                end = len(nums)-1
                while head <end:
                    if nums[head]+nums[end]+nums[i]+nums[j] == target:
                        answer.append([nums[i],nums[j],nums[head],nums[end]])
                        while head<end and nums[head]==nums[head+1]:
                            head=head+1
                        head =head+1
                        end =end - 1
                    elif nums[head]+nums[end]+nums[i]+nums[j] <target:
                        head = head+1
                    else:
                        end =end-1
        return answer


a =Solution()
print(a.fourSum([0,0,0,0],0))