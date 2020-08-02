class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        y_stack,x_minus_y_stack,x_plus_y_stack = [],[],[]
        #count = 0
        def dfs(x = 0,count = 0):
            if x==n:
                count=count + 1
                return count
            for y in range(n):
                if (y not in y_stack) and (x-y not in x_minus_y_stack) and (x+y not in x_plus_y_stack):
                    y_stack.append(y)
                    x_minus_y_stack.append(x-y)
                    x_plus_y_stack.append(x+y)
                    count = dfs(x+1,count)
                    y_stack.pop()
                    x_minus_y_stack.pop()
                    x_plus_y_stack.pop()
            return count
        count = dfs(0,0)
        return count


a =Solution()
print(a.totalNQueens(5))
