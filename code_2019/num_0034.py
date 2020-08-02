class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        head = 0
        end  = len(nums)-1
        if nums[head]== target:
            index1 = 0
        else:
            index1 = -1
        if nums[end] == target:
            index2 = 0
        else:
            index2 = -1
        if index1 == -1:
            while head<=end:
                mid = (head+end)>>1
                if nums[mid]==target:
                    if nums[mid-1]!=target:
                        index1 = mid
                        break
                    else:
                        end = mid -1
                elif nums[mid]<target:
                    head = mid +1
                else:
                    end = mid - 1
        if index1==-1:
            return [-1,-1]
        else:
            if nums[-1] == target:
                index2 = len(nums)-1
                return [index1,index2]
            head = index1
            end = len(nums)-1
            while head<=end:
                mid = (head+end)>>1
                if nums[mid]==target:
                    if nums[mid+1]!=target:
                        index2 = mid
                        break
                    else:
                        head = mid+1
                elif nums[mid]<target:
                    head = mid +1
                else:
                    end = mid - 1
        return [index1,index2]

a = Solution()
print(a.searchRange([8,8,8,8,8,12],8))


