class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x//10==0:
            return True
        else:
            y = x
            reversed_num = 0
            while True:
                #import pdb;pdb.set_trace()
                reversed_num =10*reversed_num + y%10
                y = y//10
                if y==0:
                    break
            if x == reversed_num:
                return True
            else:
                return False


a =Solution()
print(a.isPalindrome(121))