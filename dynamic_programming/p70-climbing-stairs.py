class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = []
        ways.append(1)
        ways.append(2)
        if n > 2:
            for i in range(2, n+1):
                ways.append(ways[i-1] + ways[i-2])
        return ways[n-1]