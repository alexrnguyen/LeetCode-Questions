class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # Set up array for dynamic programming. Base case for an amount of 0 is 0 coins
        dp = [amount+1]*(amount+1) # Number of coins cannot exceed amount+1
        dp[0] = 0

        for a in range(1, amount+1):
            for coin in coins:
                # Check if the coin can be used to make change for the amount
                if a - coin >= 0:
                    # Check if dp[a - coin] + 1 results in a better solution
                    dp[a] = min(dp[a - coin] + 1, dp[a])

        # If not the default value
        if dp[amount] != amount+1:
            return dp[amount]
        else:
            return -1

        # Time Complexity: O(amount * numCoins)
        # Space Complexity: O(amount)