class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows ==1:
            return s
        answer = [[] for i in range(numRows)]
        for i in range(len(s)):
            index = i%(2*numRows-2)
            if index<=numRows-1:
                answer[index].append(s[i])
            else:
                answer[2*numRows-2-index].append(s[i])
        final_answer = answer[0]
        for i in range(1,numRows):
            final_answer.extend(answer[i])
        final_answer = ''.join(final_answer)
        return final_answer



a = Solution()
x=a.convert("PAYPALISHIRING",3)
print(x)

