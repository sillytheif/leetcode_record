class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def multi(long_number,target,index):
            if target=='0':
                return '0'
            answer = ''
            carry = 0
            target = int(target)
            i = len(long_number)-1
            while i>=0:
                temp = int(long_number[i]) * target +carry
                carry = temp//10
                answer = str(temp%10) + answer
                i -=1
            if carry!=0:
                answer = str(carry)+answer
            answer = answer+index*'0'
            return answer
        def str_add(str1,str2):
            #import pdb;pdb.set_trace()
            length_1 = len(str1)-1
            length_2 = len(str2)-1
            carry = 0
            answer =''
            val_1,val_2 = 0,0
            while length_1>=0 or length_2>=0:
                if length_1>=0:
                    val_1 = int(str1[length_1])
                    length_1 -=1
                if length_2>=0:
                    val_2 = int(str2[length_2])
                    length_2-=1
                temp =val_1+val_2+carry
                carry = temp//10
                answer = str(temp%10) + answer
                val_1,val_2 = 0,0
            if carry!=0:
                answer = str(carry) +answer
            return answer
        #nimport pdb;pdb.set_trace()
        if num1=='0' or num2=='0':
            return '0'
        num1_length = len(num1)
        final=''
        for i in range(num1_length):
            final = str_add(final,multi(num2,num1[i],num1_length-1-i))
        return final


a = Solution()
print(a.multiply('123','456'))

