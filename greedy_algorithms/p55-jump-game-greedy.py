class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Greedy Solution
        # The goal is to get to the last index. Start at the second last index
        goal = len(nums) - 1
        current = len(nums) - 2
        while current >= 0:
            if current + nums[current] >= goal:
                # Change goal to current (possible to reach end from current)
                goal = current
            current = current - 1

        # Return True if we can reach the end from the first index (goal == 0)
        if goal == 0:
            return True
        else:
            return False

        # Time Complexity: O(n)
        # Space Complexity: O(1)