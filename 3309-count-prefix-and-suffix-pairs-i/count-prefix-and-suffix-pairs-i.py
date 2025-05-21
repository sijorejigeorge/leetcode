class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        result = []
        count = 0
        for i, w in enumerate(words):
            for index in range(i+1, len(words)):
                if words[i] == words[index][0: len(words[i])] and words[i] == words[index][-len(words[i]):]:
                    print(words[i], words[index])
                    count+=1
        return count

        