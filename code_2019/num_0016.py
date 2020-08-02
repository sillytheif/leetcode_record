class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        temp_min = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            head = i +1
            end =len(nums) - 1
            while head < end:
                sum = nums[head]+nums[end]+nums[i]
                if sum == target:
                    return sum
                elif sum<target:
                    head = head+1
                else:
                    end = end -1
                if abs(sum-target)<abs(temp_min-target):
                    temp_min = sum
        return temp_min


a =Solution()
print(a.threeSumClosest([-1, 2, 1, -4],1))
