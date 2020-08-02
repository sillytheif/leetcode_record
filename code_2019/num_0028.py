class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=='':
            return 0
        answer = -1
        i = 0
        while i <len(haystack):
            if haystack[i]==needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return answer