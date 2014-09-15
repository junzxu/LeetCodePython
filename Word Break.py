class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def __init__(self):
        self.Map = {}
    
    def wordBreak(self, s, dict):
        if len(s) == 0:
            return True
        if self.Map.has_key(s):
            return self.Map[s]
        for word in dict:
            if s.startswith(word):
                newS = s[len(word):]
                result = self.wordBreak(newS,dict)
                self.Map[newS] = result
                if result:
                    return True
        return False