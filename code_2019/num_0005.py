class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_length = 1
        max_begin_index = 0
        palidrome_index = 0
        i =0
        while i <=len(s):
            if i-1>=0 and s[i] == s[i-1]:
                temp_mask = 1
                while i-1-temp_mask>=0 and s[i+1+temp_mask]==s[i-1-temp_mask]:
                    temp_mask+=1
            if i-2>=0 and s[i] == s[i-2]:
                temp_mask = 1
                while i-2-temp_mask>=0 and s[i-2-temp_mask]==s[i+temp_mask]:
                    temp_mask+=1 



class Solutioon2:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        import numpy
        arr = np.adarray((len(s),len(s)))
        for  i in range(len(s)):
            for j in range(len(s)):
                if i == j:
                    arr[i][j] = 1
                else:
                    arr[i][j] = 0
        if len(s)>0:
            longest_pal = s[len[s]-1]
        else:
            return ''
        for i in range(len(s)-1):
            if s[i] ==s[i+1]:
                arr[i][i+1] = 1
                longest_pal = s[i:i+2]

        for length in range(2,len(s)-1):
            for start in range(0,len(s)-length):
                end = start +length
                if s[start] == s[end] and arr[start+1][end-1]==1:
                    arr[start][end] =1
                    longest_pal = s[start:end+1]

        return longest_pal

class Solution3():
    def longestPalindrome(self, s):
        n =len(s)
        if n<=1:
            return s
        data = [[0]*n]*n
        for i in range(n):
            data[i][i] = 1
        longest_pal = s[n-1]
        for i in range(n-1):
            if s[i]==s[i+1]:
                data[i][i+1] = 1
                longest_pal = s[i:i+2]
        for length in range(2,n-1):
            for start in range(0,n-length):
                end = start+length
                if s[start]== s[end] and data[start+1][end-1]==1:
                    data[start][end] = 1
                    longest_pal = s[start:end+1]
     return longest_pal






