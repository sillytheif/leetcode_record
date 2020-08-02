class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        attention = []
        target_index1 = 0
        target_index2 = 0
        index_len_dict ={}
        while target_index2 !=len(s):
            if s[target_index2] not in attention:
                attention.append(s[target_index2])
                #target_index2 = target_index2 +1
            else:
                temp_index = attention.index(s[target_index2])
                #import pdb;pdb.set_trace()
                for i in range(temp_index+1):
                    attention.pop(0)
                attention.append(s[target_index2])
                index_len_dict[target_index1] = target_index2 - target_index1
                target_index1 = temp_index + target_index1 +1
            target_index2 = target_index2 + 1
        #import pdb;pdb.set_trace()
        index_len_dict[target_index1] = target_index2 - target_index1
        len_list =list(index_len_dict.values())

        if len_list!=[]:
            return max(len_list)
        else:
            return len(s)


a = Solution()
print(a.lengthOfLongestSubstring(' '))
