class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        answer = []
        x = num
        if x>=1000:
            answer.append(x // 1000 * 'M')
            x =x%1000
        ten_dict = {1:'I',10:'X',100:'C',1000:'M'}
        fiv_dict = {5:'V',50:'L',500:'D'}
        init =100
        while x!=0:
            temp = x//init
            if temp!=0:
                if temp>=5:
                    if temp==9:
                        answer.append(ten_dict[init])
                        answer.append(ten_dict[10*init])
                    else:
                        answer.append(fiv_dict[5*init])
                        answer.append(ten_dict[init]*(temp-5))
                else:
                    if temp ==4:
                        answer.append(ten_dict[init])
                        answer.append(fiv_dict[5*init])
                    else:
                        answer.append(ten_dict[init]*temp)
            x =x%init
            init = init//10

        final = ''.join(answer)
        return final

a =Solution()
print(a.intToRoman(58))