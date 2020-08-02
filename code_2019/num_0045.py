class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length<=1:
            return 0
        most_far_source={}
        for i in range(0,len(nums)-1):
            for j in range(1,nums[i]+1):
                if most_far_source.get(i+j)==None and i+j<length:
                    most_far_source[i+j] = i
        count = 0
        flag = len(nums)-1
        while flag!=0:
            flag = most_far_source[flag]
            count = count +1
        return count

class Solution2:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length<=1:
            return 0
        most_far_source={}
        min_index = 0
        i = 0
        #import pdb;pdb.set_trace()
        while min_index< length-1:
            if i+nums[i] < min_index:
                i = i + 1
                continue
            for j in range(min_index+1,min(nums[i]+i+1,length)):
                most_far_source[j] = i
            min_index = nums[i]+i
            i =i+1
        count = 0
        flag = len(nums)-1
        #import pdb;pdb.set_trace()
        while flag!=0:
            flag = most_far_source[flag]
            count = count +1
        return count
a = Solution2()
print(a.jump([3,3,1,1,0,1,1,1,4]))