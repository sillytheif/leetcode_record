class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        import math
        from collections import defaultdict
        a =defaultdict(list)
        a{1}
        count =0
        for  i in digits:
            if i =='7' or i=='9':
                count +=1
        length = math.pow(3,count)* math.pow(4,count)
        answer = []
        for i in range(length):
            answer.append('')
        for x in digits:
            if x== '7' or x == '9':


