class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sqet_bit_sum(n):
            sum = 0
            while n!=0:
                temp = n%10
                sum = sum + temp**2
                n = n//10
            return sum
        x = []
        x.append(n)
        while True:
            n = sqet_bit_sum(n)
            if n == 1:
                return True
            elif n in x:
                return False
            else:
               x.append(n)

