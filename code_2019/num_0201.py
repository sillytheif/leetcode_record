class Solution2:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        while m < n: n &= n - 1
        return n
class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while(m!=n):
            m=m>>1
            n=n>>1
            i+=1
        return m<<i

a =Solution()
print(a.rangeBitwiseAnd(5,7))