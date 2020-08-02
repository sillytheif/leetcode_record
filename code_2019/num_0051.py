class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        import copy
        def solver(current,answer,state,row,col,res_number):

            temp = check(row,col,state)
            if temp==final_state:
                if res_number==0 and current not in answer:
                    answer.append(current)
                return
            for i in range(n):
                for j in range(n):
                    # only true can into check stage
                    if temp[i][j]==True:
                        a = copy.deepcopy(current)
                        a[i][j] = 'Q'
                        solver(a,answer,temp,i,j,res_number-1)
        def check(row,col,state):
            temp = copy.deepcopy(state)
            N = len(state)
            for i in range(N):
                temp[row][i] = False
                temp[i][col] = False
            for i in range(min(row, col)):
                temp[row - i - 1][col - i - 1] = False
            for i in range(N - 1 - max(row, col)):
                temp[row + i + 1][col + i + 1] = False
            for i in range(min(col, N - 1 - row)):
                temp[row + i + 1][col - i - 1] = False
            for i in range(min(row, N - 1 - col)):
                temp[row - i - 1][col + i + 1] = False
            return temp
        answer = []
        current = [['.' for i in range(n)] for i in range(n)]
        init_state = [[True for i in range(n)] for i in range(n)]
        final_state = [[False for i in range(n)] for i in range(n)]
        #solver(current, answer, init_state, 0, 1, n-1)
        for i in range(n):
            for j in range(n):
                a = copy.deepcopy(current)
                a[i][j] ='Q'
                solver(a, answer, init_state, i, j, n-1)
                #import pdb;pdb.set_trace()
        final_answer = []
        for x in answer:
            final_answer.append([])
            for y in x:
                #print(y)
                #print(''.join(y))
                final_answer[-1].append(''.join(y))
        return final_answer


#a = [[True for i in range(4)] for i in range(4)]
#print(check(2,1,a))
a =Solution()
print(a.solveNQueens(5))


class Solution2 :
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res, y_stack, x_minus_y_stack, x_plus_y_stack = [], [], [], []

        def dfs(x=0):
            if x == n:
                res.append(['.' * y + 'Q' + '.' * (n - 1 - y) for y in y_stack])
                return
            for y in range(n):
                if (y not in y_stack) and (x - y not in x_minus_y_stack) and (x + y not in x_plus_y_stack):
                    y_stack.append(y)
                    x_minus_y_stack.append(x - y)
                    x_plus_y_stack.append(x + y)
                    dfs(x + 1)  # increasing depth
                    y_stack.pop()
                    x_minus_y_stack.pop()
                    x_plus_y_stack.pop()

        dfs()  # default is x = 0
        return res