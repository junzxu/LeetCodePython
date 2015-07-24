class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        dup_count = 0
        pre = 0
        cur = 1
        while cur < len(A):
            if A[pre] != A[cur]:
                pre += 1
                A[pre] = A[cur]
                dup_count = 0
            else:
                dup_count += 1
                if dup_count == 1:
                    pre += 1
                    A[pre] = A[cur]
            cur += 1
        return pre+1