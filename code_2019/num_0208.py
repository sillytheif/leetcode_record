class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.structure=[]
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        self.structure.append(word)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word in self.structure:
            return True
        else:
            return False
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        n = len(prefix)
        for x in self.structure:
            if x[0:n]==prefix:
                return True
        return False