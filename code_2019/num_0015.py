class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        if len(nums) <3:
            return []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count+=1
        if count>=3:
            answer.append([0,0,0])
        wait_answer = [-x for x in nums]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                temp = nums[i] + nums[j]
                if (temp in wait_answer and nums[i]!=-2*nums[j] and nums[j]!=-2*nums[i]) :
                   temp = sorted([nums[i],nums[j],-nums[i]-nums[j]])
                   if temp not in answer:
                       answer.append(temp)
        return answer




class Solution2:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        answer = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            head = i+1
            end = len(nums)-1
            while head<end:
                if nums[head]+nums[end] == target:
                    answer.append([nums[i],nums[head],nums[end]])
                    while head<end and nums[head]==nums[head+1]:
                        head = head+1
                    while head<end and nums[end]==nums[end-1]:
                        end = end -1
                    head = head +1
                    end  = end  -1
                elif nums[head]+nums[end] < target:
                    head = head+1
                else:
                    end  = end-1

        return answer

a =Solution2()
print(a.threeSum([-1,0,1,2,-1,-4]))