class Solution:
  def minCut(self,s):
    length=len(s)
    is_palindrome=[[False for _ in xrange(length)] for _ in xrange(length)] #indicate if s[j:i] is palindrome
    DP_minCut=[length for _ in xrange(length)] # the minimum cut that cuts s[0:i]

    for i in xrange(0,length):
      for j in xrange(0,i+1):
        if (s[j]==s[i])and((is_palindrome[j+1][i-1] if (i>0 and j<length-1 )else False) or i-j<2):
          is_palindrome[j][i]=True
          if j==0:DP_minCut[i]=0
          DP_minCut[i]=min(DP_minCut[i],DP_minCut[j-1]+1)

    return DP_minCut[-1]