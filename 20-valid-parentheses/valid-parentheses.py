class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        for i in s:
            
            if i == "(":
                st.append(")")
            if i == "[":
                
                st.append("]")
                
            if i == "{":
                st.append("}")
            if i == ")":
                if not st:
                    return False
                t = st.pop()
                if t != ")":
                    return False
            if i == "]":
                if not st:
                    return False
                t = st.pop()
                if t != "]":
                    return False
            if i == "}":
                if not st:
                    return False
                t = st.pop()
                if t != "}":
                    return False
            
        if not st:
            return True
        else:
            return False

