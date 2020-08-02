class Solution():
class Solution:
    def permute_BFS(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        state_list = [{'pre':[],'rest':set(nums)}] # init
        for _ in range(len(nums)): # max count
            new_state_list = []
            for dic in state_list:
                for num in dic['rest']:
                    # pick one number from dic['rest'] and append it to dic['pre']
                    new_state_list.append({'pre':dic['pre']+[num],'rest':dic['rest']-{num}})
            state_list = new_state_list # update state_list
        return [x['pre'] for x in state_list]
    
    def permute_DFS(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def get_rest(result_list, pre_list, rest_set):
            if not rest_set: # no numbers left
                result_list.extend(pre_list)
            for i in rest_set: # pick one number and recur the remains
                get_rest(result_list, [x+[i] for x in pre_list], rest_set-{i})
        result_list = []
        get_rest(result_list, [[]], set(nums))
        return result_list
