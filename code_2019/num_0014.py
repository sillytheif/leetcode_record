class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) ==1:
            return strs[0]
        length = [len(x) for x in strs]
        min_length = min(length)
        #answer = []
        attention = []
        flag = 0
        #import pdb;pdb.set_trace()
        for i in range(min_length):
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    flag = 1
                    break
            if flag == 0:
                attention.append(strs[0][i])
            if flag == 1:
                break
        #import pdb;pdb.set_trace()
        final = ''.join(attention)
        return final

a = Solution()
print(a.longestCommonPrefix(['aca','cba']))