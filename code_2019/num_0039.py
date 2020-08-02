class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        answer = []
        def search(sum,answer,index,path):
            if sum == 0:
                answer.append(path)
                return
            if sum<0:
                return
            for i in range(index,len(candidates)):
                search(sum-candidates[i],answer,i,path+[candidates[i]])
        search(target,answer,0,[])
        return answer


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()

        def dfs(target, index, path):
            if target < 0:
                return  # backtracking
            if target == 0:
                res.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(target - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return res