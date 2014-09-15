class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def __init__(self):
        self.Cache = {}
        
    def wordBreak(self, s, dict):
        if not s:
            return []
        result = []
        for word in dict:
            if s.startswith(word):
                new_s = s[len(word):]
                if new_s == "":
                    result.append(word)
                if not self.check(new_s,dict):
                    continue
                partial = self.wordBreak(new_s,dict)
                for seq in partial:
                    sentence = word + ' ' + seq
                    result.append(sentence)
        return result

    def check(self, s, dict):
        # check if s can construct a sentence and cache the result
        if len(s) == 0:
            return True
        if self.Cache.has_key(s):
            return self.Cache[s]
        for word in dict:
            if s.startswith(word):
                newS = s[len(word):]
                result = self.check(newS,dict)
                self.Cache[newS] = result
                if result:
                    return True
        return False