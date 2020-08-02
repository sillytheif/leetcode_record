class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ten_dict = {'I':1,'X':10,'C':100,'M':1000}
        fiv_dict = {'V':5,'L':50,'D':500}
        i =0
        sum = 0
        temp = 0
        while i<len(s):
            if ten_dict.get(s[i]) != None:
                if ten_dict.get(s[i]) == 10*temp:
                    sum = sum + 8*temp
                else:
                    sum = sum + ten_dict.get(s[i])
                temp = ten_dict.get(s[i])
            else:
                if fiv_dict[s[i]] ==  5*temp:
                    sum = sum +3*temp
                else:
                    sum = sum+fiv_dict[s[i]]

                temp = fiv_dict[s[i]]
            i = i+1
        return sum

a =Solution()
print(a.romanToInt('MCMXCIV'))
