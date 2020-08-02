class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # the solution should be appended in the below list
        result = []

        # ignoring any action if the string or the list of words has 0 length
        if len(s) == 0 or len(words) == 0:
            return result

        from collections import Counter

        word_length = len(words[0])
        words_count = len(words)

        # the window size that we are going to slide
        window_length = words_count * word_length

        # temp list to store splitted window size part of the string
        temp = []

        # checking from 0 till word length before the sting end
        for i in range(0, len(s) - window_length + 1):
            # the sliding window from the string to be checked against the words
            word_window = s[i:i + window_length]
            # splitting the window string to a list of splitted words
            temp = [word_window[j:j + word_length] for j in range(0, window_length, word_length)]
            # checking if the splitted words and original words are the same
            if Counter(temp) == Counter(words):
                # append the value of i which is the index of the first letter in the sliding window
                result.append(i)

        return result