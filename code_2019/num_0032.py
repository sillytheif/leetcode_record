class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        import numpy as np
        if len(s)==0 and len(s)==1:
            return 0
        if len(s)==2:
            if s[0]=='(' and s[1]==')':
                return 2
            else:
                return 0
        data = np.ndarray(shape=len(s),dtype=int)
        for i in range(len(s)):
            data[i] = 0
        for i in range(len(s)):
            if s[i] == ')':
                if i-1>=0 and s[i-1] == '(':
                    if i>=2:
                        data[i] = data[i-2]+2
                    else:
                        data[i] = 2
                elif i-data[i-1]>0 and s[i-data[i-1]-1]=='(':
                    if i-data[i-1]>=2:
                        data[i] = data[i-1] + data[i-data[i-1]-2] +2
                    else:
                        data[i] = data[i-1] + 2
        #import pdb;pdb.set_trace()
        return int(max(data))

class Solution2():
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int(
        """
        stack = []
        stack.append(-1)
        max_length = 0
        current_length = 0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop(-1)
                if len(stack)==0:
                    stack.append(i)
                else:
                    max_length = max(max_length,i-stack[-1])
        return max_length
a = Solution2()
print(a.longestValidParentheses("()(()"))
