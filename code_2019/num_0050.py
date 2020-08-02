class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n ==1:
            return 1
        def pow_self(x,mi):
            if mi<0:
                return 1/pow_self(x,-mi)
            if mi==1:
                return x
            if mi==0:
                return 1
            son_mi = mi>>1
            answer = pow_self(x,son_mi)*pow_self(x,son_mi)
            if mi&0x1==0:
                return answer
            else:
                return x*answer

        return pow_self(x,z)

a =Solution()
print(a.myPow(2,10))