class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = s.strip().split()
        words = words[::-1]
        reverse = " ".join(words)
        return reverse