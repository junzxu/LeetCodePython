class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
        
    def ladderLength(self, start, end, dict):
        char = [chr(c) for c in range(97, 123)] #characters from a to z
        if not start or not end or not dict or not len(start) or not len(dict):
            return 0
        if start == end:
            return 0
        queue = [[start, 1]] 
        dist = set([start])
        #BFS
        while queue:
            word, dis = queue.pop(0)
            dis += 1
            for i in range(len(word)):
                for c in char:
                    nw = word[:i] + c + word[i+1:]
                    if nw == end:
                        return dis 
                    if nw in dict and nw not in dist:
                        queue.append([nw, dis])
                        dist.add(nw)
        return 0