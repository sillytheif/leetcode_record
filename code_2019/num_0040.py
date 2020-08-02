class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def search(sum,path,index,res):
            if sum==0:
                if path not in res:
                    res.append(path)
            if sum<0:
                return
            for i in range(index+1,len(candidates)):
                search(sum-candidates[i],path+[candidates[i]],i,res)
        answer = []
        candidates.sort()
        search(target,[],-1,answer)
        return answer

a =Solution()
print(a.combinationSum2([2,5,2,1,2],5))