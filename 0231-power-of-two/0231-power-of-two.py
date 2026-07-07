class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''found=False
        for i in range(n):
            if 2**i==n:
                return True
                break
        if not found:
            return False'''
        if n==1:
            return True
        if n <= 0 or n % 2 != 0:
            return False
        return self.isPowerOfTwo(n // 2)