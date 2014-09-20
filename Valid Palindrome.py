class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        chars = [char for char in s.lower() if 97<=ord(char)<=123 or 48<=ord(char)<=57]
        if not chars:
            return True #if s is empty or contains only spaces
        hi = len(chars)-1
        lo = 0
        while lo <= hi:
            if chars[lo] != chars[hi]:
                return False
            lo += 1
            hi -= 1
        return True