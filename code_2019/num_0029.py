class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend < 0:
            x = -dividend
        else:
            x = dividend
        if divisor < 0:
            y = -divisor
        else:
            y = divisor
        if x < y:
            return 0
        count = 0
        temp_y = y
        y_list = []
        count_dict = {}
        count = 1
        while temp_y <= x:
            y_list.append(temp_y)
            count_dict[temp_y] = count
            temp_y = temp_y + temp_y
            count = count + count
        count = 0
        temp_y = y_list.pop(-1)
        while x > 0:
            if x >= temp_y:
                count = count + count_dict[temp_y]
                x = x - temp_y

            if len(y_list) == 0:
                break
            temp_y = y_list.pop(-1)
        if (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0):
            count = count
        else:
            count = -count
        if count > 2147483647 or x < -2147483648:
            return 2147483647
        return count