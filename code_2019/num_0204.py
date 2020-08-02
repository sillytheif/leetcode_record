class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        def is_primes(n):
            end = int(math.sqrt(n))
            for i in range(2,end+1):
                if n%i==0:
                    return 0
            return 1
        count = 0
        for i in range(2,n):
            count+=is_primes(i)
        return count

class Solution2():
    def countPrimes(self,n):
        if n<3:
            return 0
        primes =[True]*n
        primes[0] = primes[1] =False
        for i in range(2,int(n**0.5)+1):
            if primes[i]:
                primes[i**2:n:i] = [False]*len(primes[i**2:n:i])
        return sum(primes)
a =Solution()
print(a.countPrimes(3))
# def is_primes(n):
#     import math
#     end = int(math.sqrt(n))
#     for i in range(2,end+1):
#         if n%i==0:
#             return 1
#     return 0
#
# print(is_primes(4))