class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        attention =[]
        my_dict = {']':'[' , '}':'{', ')':'('}
        for x in s:
            #import pdb;pdb.set_trace()
            if x==')' or x=='}' or x ==']':
                if attention==[] or attention.pop(-1)!=my_dict[x]:
                    return False
            else:
                attention.append(x)
        if attention == []:
            return True
        else:
            return False


a =Solution()
print(a.isValid('([)]'))