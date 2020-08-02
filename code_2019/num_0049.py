class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        set_list = []
        answer = []
        for x in strs:
            m = sorted(x)
            if m not in set_list:
                set_list.append(m)
                answer.append([])
            answer[set_list.index(m)].append(x)
        return answer
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_ = {}
        res = []
        for i in range(len(strs)):
            mid = str(sorted(strs[i]))
            if mid in dict_.keys():
                dict_[mid].append(strs[i])
            else:
                dict_[mid] = []
                dict_[mid].append(strs[i])
        for item in dict_.keys():
            res.append(dict_[item])
        return res
a =Solution()
print(a.groupAnagrams(["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]))