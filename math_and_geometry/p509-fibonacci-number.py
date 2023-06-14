class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Memoization Solution
        if n == 0 or n == 1:
            return n
        
        if n in fib_nums:
            return fib_nums[n]
        fib_nums[n] = self.fib(n - 1) + self.fib(n - 2)
        return fib_nums[n]

fib_nums = {} # Global