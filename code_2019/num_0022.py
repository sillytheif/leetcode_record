class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(left=0,right=0,result =''):
            if len(result)==2*n:
                answer.append(result)
                return
            if left<n:
                generate(left+1,right,result+'(')
            if right<left:
                generate(left,right+1,result+')')
        answer =[]
        generate()
        return answer