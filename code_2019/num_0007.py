class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        if x>math.pow(2,31)-1 or x < -math.pow(2,31):
            return 0
        else:
            if x<0:
                y =-x
            else:
                y = x
            reversed_num = 0
            while True:
                #import pdb;pdb.set_trace()
                reversed_num = 10*reversed_num + y%10
                y = y//10
                if y==0:
                    break
            if reversed_num > math.pow(2, 31) - 1 or reversed_num < -math.pow(2, 31):
                return 0
            if x>=0:
                return reversed_num
            else:
                return -reversed_num


a = Solution()
print(a.reverse(1534236469))

