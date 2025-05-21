class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for i, w in enumerate(words):
            for index, s in enumerate(words):
                if i != index:
                    if w in s:
                        result.append(w)
                        break
                        
        return result

    


        