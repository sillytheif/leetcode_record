class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        if len(t)!=n:
            return False
        a_dict ={}
        for i in range(n):
            if s[i] not in a_dict.keys() and:
                a_dict[s[i]]=t[i]
            else:
                if a_dict[s[i]]!=t[i]:
                    return False
        return True