class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        """
        # Brute Force Solution (O(n^2) time)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
        """    
        
        # Hash Table Solution (O(n) time)
        table = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in table and table[target-num] != i:
                return [table[target - num], i]
            table[num] = i