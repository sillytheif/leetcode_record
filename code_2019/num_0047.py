class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        now = []
        def search(current,res,results):
            if res == []:
                results.append(current)
                return
            for i in range(len(res)):
                if i>0 and res[i]==res[i-1]:
                    continue
                temp = res.pop(i)
                search(current+[temp],res,results)
                res.insert(i,temp)
        search(now,nums,results)
        return results

a =Solution()
print(a.permuteUnique([1,1,2]))
